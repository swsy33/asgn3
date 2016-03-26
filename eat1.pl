/*can(Action, Precond).adds(Action, EffP).deletes(Action, EffN).*/
can(open(X),[cl(X), closed(X)]).
adds(open(X),[opened(X)]).
deletes(open(X),[closed(X)]).

can(close(X),[cl(X), opened(X)]).
adds(close(X),[closed(X)]).
deletes(close(X),[opened(X)]).

can(take(X, From),[in(X,From), cl(From), opened(From)]).
adds(take(X, From),[has(X)]).
deletes(take(X, From),[in(X, From)]).

can(putIn(C, In), [has(C), opened(In), cl(In)]).
adds(putIn(C, In),[in(C, In)]).
deletes(putIn(C, In),[has(C)]).

can(bake(X),[in(X, mo), closed(mo), cl(mo)]).
adds(bake(X),[baked(X)]).
deletes(bake(X),[]).

can(eat(X),[baked(X), has(X)]).
adds(eat(X),[in(X, G), not_hungry]).
deletes(eat(X),[has(X)]).

can(move(To),[]).
adds(move(To),[cl(To)]).
deletes(move(To),[]).
