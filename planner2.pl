
plan(State, Goals, [], State):- satisfied(State, Goals).
plan(State, Goal, Plan, FinalState):- conc(Plan,_,_), conc(PrePlan, [Action|PostPlan], Plan), select(State, Goals, Goal), achieves(Action, Goal), can(Action, Conditions), plan(State, Conditions, PrePlan, MidState1), apply(Action, MidState1, MidState2),plan(MidState2, Goals, PostPlan, FinalState).

satisfied(State, []).
satisfied(State, [Goal|Goals]):- member(Goal, State), satisfied(State,Goals).

select(State, Goals, Goal):- member(Goal, Goals),\+member(Goal, State).

achieves(Action, Goal):- adds(Action, Goals), member(Goal, Goals).

apply(State, Action, NewState):- deletes(Action, DelList), delete_all(State,DelList,State),!, adds(Action,AddList),conc(AddList,State1, NewState).

delete_all([],_,[]).
delete_all([X|L1], L2, Diff):- member(X, L2),!,delete_all(L1,L2,Diff).
delete_all([X|L1],L2,[X|Diff]):- delete_all(L1,L2,Diff).

conc([],X,X).
conc([],[],[]).
conc(X,[],X).
conc([X|R],T,[X|S]) :- conc(R,T,S).