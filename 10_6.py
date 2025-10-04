male(john).
male(mike).
male(david).
female(lisa).
female(susan).
female(anna).

parent(john,mike).
parent(john,lisa).
parent(susan,mike).
parent(susan,lisa).
parent(mike,david).
parent(anna,david).

father(F,C):-male(F),parent(F,C).
mother(M,C):-female(M),parent(M,C).

grandfather(GF,C):-male(GF),parent(GF,P),parent(P,C).
grandmother(GM,C):-male(GM),parent(GM,P),parent(P,C).

sibling(X,Y):- parent(P,X),parent(P,Y),X\=Y.