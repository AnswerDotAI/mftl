---
title: "Appendix 1: Utilities"
anchor: "appendix-1-utilities"
previous: "supplement.html"
next: "references.html"
---

```
and      =:  *.                             NB. 13B 
ant      =: 0:,] % next i. on #             NB. 18C                     
anti     =:  d. _1                          NB. 18A 
cos      =:  2&o.                           NB. 19D
cube     =:  ^ with 3                       NB. 14G                        

dec      =:  rat^:_1                        NB. 2A  
der      =:  1: |. ] * i. on #              NB. 6B  
derv     =:  d.1                            NB. 18A 
decay    =:  ^ on -                         NB. 8C
det      =:  -/ . *                         NB. 20B 

diag     =:  /.                             NB. 11F
dp       =:  +/ . *                         NB. 15A 
each     =:  "0                             NB. 11F
eachbox  =:  &.>                            NB. 11F
eachrow  =: "1                              NB. 13D

exp      =:  ^                              NB. 6C
for      =:  ^:                             NB. 1C
gcd      =:  +.                             NB. 2E
INV      =:  ^:_1                           NB. 9A
lcm      =:  *.                             NB. 2E         

load 'plot'                                 NB. 3A  
mean     =:  +/ % #                         NB. 9C  
next     =:  >:                             NB. 1A
not      =:  -.                             NB. 13B         
on       =:  @                              NB. 2D

or       =:  +.                             NB. 13B 
over     =: 2 :'(u.@v.)=((u.@[)v.(u.@]))'"0 NB. 14E
pa       =:  p.                             NB. 16A                 
pc       =:  +//. on (*/)                   NB. 16B 
pd       =:  |. on [ pa ]                   NB. 16A 

PLOT     =: 'line,stick'&plot               NB. 3A  
pref     =:  \                              NB. 11F
previous =:  <:                             NB. 1A 
pw       =:  1 : '2 with (u.\)'             NB. 3C  
rat      =:  x:                             NB. 2A

roots    =:  > on {: on p.                  NB. 9E 
set      =:  9!:11                          NB. 2B  
sign     =:  *                              NB. 2D 
sin      =:  1&o.                           NB. 5B  
sort     =:  /:~                            NB. 12A

sqr      =:  *:                             NB. 9A
sqrt     =:  %:                             NB. 9A 
sum      =:  +/                             NB. 11F
trans    =:  |:                             NB. 12A
under    =:  &.                             NB. 10D 

with     =:  &                              NB. 1F  
zero     =:  **|                            NB. 9E
```
