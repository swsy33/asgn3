open(X)
PREC = [cl(X), closed(X)]
Eff+ = [opened(X)]
Eff- = [closed(X)]

close(X) 
PREC = [cl(X), opened(X)]
Eff+ = [closed(X)]
Eff- = [opened(X)]

take(X, From) 
PREC = [in(X,From), cl(From), opened(From)]
Eff+ = [has(X)]
Eff- = [in(X, From)]

putIn(C, In) 
PREC = [has(C), opened(In), cl(In)]
Eff+ = [in(C, In)]
Eff- = [has(C)]

bake(X) 
PREC = [in(X, mo), closed(mo), cl(mo)]
Eff+ = [baked(X)]
Eff- = []

eat(X) 
PREC = [baked(X), has(X)]
Eff+ = [not_hungry]
Eff- = [has(X)]

move(To) 
PREC = []
Eff+ = [cl(To)]
Eff- = []
