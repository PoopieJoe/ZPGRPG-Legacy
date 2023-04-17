from __future__ import annotations
from typing import Type,TypeVar,Any
from abc import ABC, abstractmethod

import src.lib as lib


### https://github.com/sploreg/goap (goap/Assets/Standard Assets/Scripts/AI)

class GOAP:
    
    
    class Agent:
        statemachine        : GOAP.FSM

        idleState           : GOAP.FSM.State
        moveToState         : GOAP.FSM.State
        performActionState  : GOAP.FSM.State

        availableActions    : list[GOAP.Action]
        currentActions      : list[GOAP.Action]

        planner             : GOAP.Planner

        world               : lib.world.World

        def start(self,
                  world     : lib.world.World):
            self.world = world
            self.statemachine = GOAP.FSM()
            self.availableActions = []
            self.currentActions = []
            self.planner = GOAP.Planner()
            self.findDataProvider()
            self.createStates()
            self.statemachine.push(self.idleState)
            self.loadActions()
        
        def update(self):
            self.statemachine.update(self.world)
        
        def addAction(self,
                      action    : GOAP.Action):
            self.availableActions.append(action)

        def getAction(self,
                      actionType    : Type[TAction]) -> TAction | None:
            for action in self.availableActions:
                if isinstance(action,actionType):
                    return action
            return None
        
        def removeAction(self,
                         action    : GOAP.Action):
            self.availableActions.remove(action)

        def hasActionPlan(self):
            return self.currentActions.__len__() > 0
        
        def createStates(self):
            class IdleState(GOAP.FSM.State):
                def update(self, fsm: GOAP.FSM, world: lib.world.World):
                    return super().update(fsm, world)
            raise NotImplementedError
        
        def findDataProvider(self):
            raise NotImplementedError
        
        def loadActions(self):
            raise NotImplementedError

    class Action:
        _preconditions : dict[str,Any]
        _postconditions : dict[str,Any]
        _inRange : bool = False

        cost : float = 1
        target : lib.entity.Entity | None = None

        def planReset(self):
            self._inRange = False
            self.target = None
            self.reset()

        @abstractmethod
        def reset(self):
            pass

        @abstractmethod
        def isDone(self):
            pass

        @abstractmethod
        def checkProceduralPreconditions(self, worldObject : lib.world.World, actor : lib.character.Character) -> bool:
            pass

        @abstractmethod
        def perform(self, worldObject : lib.world.World) -> bool:
            pass

        @property
        @abstractmethod
        def requiresInRange(self) -> bool:
            pass

        @property
        def inRange(self) -> bool:
            return self._inRange
        
        @inRange.setter 
        def inRange(self,
                    value : bool):
            self._inRange = value

        def addPreCondition(self,
                            key : str, 
                            value : bool):
            self._preconditions.update({key:value})

        def removePreCondition(self,
                               key : str):
            self._preconditions.pop(key)

        def addPostCondition(self,
                            key : str, 
                            value : bool):
            self._postconditions.update({key:value})

        def removePostCondition(self,
                               key : str):
            self._postconditions.pop(key)

        @property
        def preconditions(self):
            return self._preconditions
        
        @property
        def postconditions(self):
            return self._preconditions


    class Planner:
        class Node:
            parent      : GOAP.Planner.Node | None
            runningCost : float
            state       : dict[str,Any]
            action      : GOAP.Action | None

            def __init__(self,
                         parent      : GOAP.Planner.Node | None,
                         runningCost : float,
                         state       : dict[str,Any],
                         action      : GOAP.Action | None) -> None:
                self.parent = parent
                self.runningCost = runningCost
                self.state = state
                self.action = action

        def plan(self,
                 agent              : lib.character.Character,
                 availableActions   : list[GOAP.Action],
                 world              : lib.world.World,
                 worldState         : dict[str,bool],
                 goalState          : dict[str,bool]) -> list[GOAP.Action]:
            
            # reset all actions
            for action in availableActions:
                action.planReset()

            # fetch all usableactions
            usableActions = [action for action in availableActions if action.checkProceduralPreconditions(world,agent)]

            # build tree and record leaf nodes that provide a valid solution to the goalState in leaves
            start = GOAP.Planner.Node(None,0,worldState,None)
            leaves : list[GOAP.Planner.Node] = []

            if (not self.buildGraph(start,leaves,usableActions,goalState)):
                return []

            # get the cheapest leaf node
            cheapest = None
            for leaf in leaves:
                if (cheapest == None) or (leaf.runningCost < cheapest.runningCost):
                    cheapest = leaf
                    
            # from this node work back to its parent nodes and fill the action plan
            actionPlan : list[GOAP.Action] = []
            node = cheapest
            while node != None:
                if node.action != None:
                    actionPlan.insert(0,node.action)
                node = node.parent

            return actionPlan

        # recursive function that explores actions until if finds a path to the desired state is achieved
        def buildGraph(self,
                       parent           : Node,
                       leaves           : list[Node],
                       usableActions    : list[GOAP.Action],
                       goalState        : dict[str,bool]) -> bool:
            
            found = False

            # see if we can use an action here
            for action in usableActions:
                if self.inState(action.preconditions, parent.state):
                    currentstate = self.populateState(parent.state, action.postconditions)

                    node = GOAP.Planner.Node(parent,
                                             parent.runningCost + action.cost,
                                             currentstate,
                                             action)
                    
                    if self.inState(goalState, currentstate):
                        leaves.append(node)
                        found = True
                    else:
                        subset = self.actionSubset(usableActions, action)
                        if (self.buildGraph(node,
                                            leaves,
                                            subset,
                                            goalState)):
                            found = True

            return found
        
        def actionSubset(self,
                         actions    : list[GOAP.Action],
                         removeMe   : GOAP.Action) -> list[GOAP.Action]:
            actions.remove(removeMe)
            return actions
        
        def inState(self,
                    test    : dict[str,bool],
                    state   : dict[str,bool]) -> bool:
            
            for t in test.items():
                if t not in state.items():
                    return False
            return True
            
        def populateState(self,
                          currentState  : dict[str,Any],
                          stateChange   : dict[str,Any]) -> dict[str,Any]:
            currentState.update(stateChange)
            return currentState
        


    class FSM:
        class State:
            @abstractmethod
            def update(self,
                    fsm      : GOAP.FSM,
                    world    : lib.world.World):
                pass

        stateStack : list[State]

        def update(self,
                world    : lib.world.World):
            self.stateStack[-1].update(self,world)

        def push(self,
                state  : State):
            self.stateStack.append(state)

        def pop(self):
            self.stateStack.pop()

TAction = TypeVar("TAction",bound=Type[GOAP.Action])