
% This program is a simple "means-ends" planner.
% Author: I. Bratko
% Source: I. Bratko, PROLOG Programming for Artificial Intelligence,
%         2nd ed.
%
plan(State,Goals,[],State):- satisfied(State,Goals).
plan(State,Goals,Plan,FinalState):-
  conc(PrePlan,[Action|PostPlan],Plan),
  select(State,Goals,Goal),
  achieves(Action,Goal),
  can(Action,Condition),
  plan(State,Condition,PrePlan,MidState1),
  apply(MidState1,Action,MidState2),
  plan(MidState2,Goals,PostPlan,FinalState).

satisfied(State,[]).
satisfied(State,[Goal|Goals]):-
  member(Goal,State), satisfied(State,Goals).

select(State,Goals,Goal):-
 member(Goal,Goals), not(member(Goal,State)).

achieves(Action,Goal):-
  add(Action,Goals),
  member(Goal,Goals).

apply(State,Action,NewState):-
  del(Action,DelList), delete(State,DelList,State1),!,
  add(Action,AddList),
  conc(AddList,State1,NewState).

delete([],_,[]).
delete([X|L1],L2,Diff):- member(X,L2),!, delete(L1,L2,Diff).
delete([X|L1],L2,[X|Diff]):- delete(L1,L2,Diff).

member(X,[X|Rest]).
member(X,[Y|Rest]):- member(X,Rest).

conc([],L,L).
conc([X|L],L1,[X|L2]):-conc(L,L1,L2).

not(P):-P,!,fail; true.
