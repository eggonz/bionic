# **Mark**down: **Syn**tax

~~**striket**hrough~~

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**tion.

# **Mark**down: **Syn**tax

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**tion.

# **Mark**down: **Syn**tax

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**tion.

# **Mark**down: **Syn**tax

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**tion.

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**tion.

**Note:** **Th**is **docu**ment **i**s **its**elf **writ**ten **usi**ng **Mark**down; **yo**u
**ca**n [**se**e **th**e **sou**rce **fo**r **i**t **b**y **add**ing '.**tex**t' **t**o **th**e **UR**L](/projects/markdown/syntax.text).

----

## **Over**view

### **Philo**sophy

**Mark**down **i**s **inte**nded **t**o **b**e **a**s **ea**sy-**t**o-**re**ad **an**d **ea**sy-**t**o-**wri**te **a**s **i**s **feas**ible.

**Readab**ility, **howe**ver, **i**s **empha**sized **abo**ve **al**l **el**se. **A** **Mark**down-**forma**tted
**docu**ment **sho**uld **b**e **publis**hable **a**s-**i**s, **a**s **pla**in **te**xt, **with**out **look**ing
**li**ke **it**'s **be**en **mar**ked **u**p **wi**th **ta**gs **o**r **forma**tting **instru**ctions. **Whi**le
**Markd**own's **syn**tax **ha**s **be**en **influ**enced **b**y **seve**ral **exis**ting **te**xt-**t**o-**HT**ML
**filt**ers -- **inclu**ding [**Set**ext](http://docutils.sourceforge.net/mirror/setext.html), [**at**x](http://www.aaronsw.com/2002/atx/), [**Text**ile](http://textism.com/tools/textile/), [**reStruct**uredText](http://docutils.sourceforge.net/rst.html),
[**Gruta**text](http://www.triptico.com/software/grutatxt.html), **an**d [**EtT**ext](http://ettext.taint.org/doc/) -- **th**e **sin**gle **bigg**est **sou**rce **o**f
**inspir**ation **fo**r **Markd**own's **syn**tax **i**s **th**e **for**mat **o**f **pla**in **te**xt **ema**il.

## **Blo**ck **Elem**ents

### **Parag**raphs **an**d **Li**ne **Bre**aks

**A** **parag**raph **i**s **sim**ply **on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt, **separ**ated
**b**y **on**e **o**r **mo**re **bla**nk **lin**es. (**A** **bla**nk **li**ne **i**s **an**y **li**ne **th**at **loo**ks **li**ke **a**
**bla**nk **li**ne -- **a** **li**ne **conta**ining **noth**ing **bu**t **spa**ces **o**r **ta**bs **i**s **consi**dered
**bla**nk.) **Nor**mal **parag**raphs **sho**uld **no**t **b**e **inde**nted **wi**th **spa**ces **o**r **ta**bs.

**Th**e **implic**ation **o**f **th**e "**on**e **o**r **mo**re **consec**utive **lin**es **o**f **te**xt" **ru**le **i**s
**th**at **Mark**down **supp**orts "**ha**rd-**wrap**ped" **te**xt **parag**raphs. **Th**is **diff**ers
**signifi**cantly **fr**om **mo**st **oth**er **te**xt-**t**o-**HT**ML **forma**tters (**inclu**ding **Mova**ble
**Typ**e's "**Conv**ert **Li**ne **Bre**aks" **opt**ion) **whi**ch **trans**late **eve**ry **li**ne **bre**ak
**chara**cter **i**n **a** **parag**raph **in**to **a** `<br />` **ta**g.

**Wh**en **yo**u ***d**o* **wa**nt **t**o **ins**ert **a** `<br />` **bre**ak **ta**g **usi**ng **Mark**down, **yo**u
**en**d **a** **li**ne **wi**th **tw**o **o**r **mo**re **spa**ces, **th**en **ty**pe **ret**urn.

### **Head**ers

**Mark**down **supp**orts **tw**o **sty**les **o**f **head**ers, [**Set**ext] [1] **an**d [**at**x] [2].

**Optio**nally, **yo**u **ma**y "**clo**se" **at**x-**sty**le **head**ers. **Th**is **i**s **pur**ely
**cosm**etic -- **yo**u **ca**n **us**e **th**is **i**f **yo**u **thi**nk **i**t **loo**ks **bet**ter. **Th**e
**clos**ing **has**hes **don**'t **ev**en **ne**ed **t**o **mat**ch **th**e **num**ber **o**f **has**hes
**us**ed **t**o **op**en **th**e **hea**der. (**Th**e **num**ber **o**f **open**ing **has**hes
**deter**mines **th**e **hea**der **lev**el.)


### **Blockq**uotes

**Mark**down **us**es **ema**il-**sty**le `>` **chara**cters **fo**r **blockq**uoting. **I**f **you**'re
**fami**liar **wi**th **quot**ing **pass**ages **o**f **te**xt **i**n **a**n **ema**il **mess**age, **th**en **yo**u
**kn**ow **ho**w **t**o **cre**ate **a** **block**quote **i**n **Mark**down. **I**t **loo**ks **be**st **i**f **yo**u **ha**rd
**wr**ap **th**e **te**xt **an**d **pu**t **a** `>` **bef**ore **eve**ry **li**ne:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
> **consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
> **Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
>
> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
> **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Mark**down **all**ows **yo**u **t**o **b**e **la**zy **an**d **on**ly **pu**t **th**e `>` **bef**ore **th**e **fir**st
**li**ne **o**f **a** **ha**rd-**wrap**ped **parag**raph:

> **Th**is **i**s **a** **block**quote **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or **si**t **am**et,
**consec**tetuer **adipi**scing **el**it. **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus.
**Vesti**bulum **en**im **wi**si, **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.

> **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it. **Suspen**disse
**i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Blockq**uotes **ca**n **b**e **nes**ted (**i**.**e**. **a** **block**quote-**i**n-**a**-**block**quote) **b**y
**add**ing **addit**ional **lev**els **o**f `>`:

> **Th**is **i**s **th**e **fir**st **lev**el **o**f **quot**ing.
>
> > **Th**is **i**s **nes**ted **block**quote.
>
> **Ba**ck **t**o **th**e **fir**st **lev**el.

**Blockq**uotes **ca**n **cont**ain **oth**er **Mark**down **elem**ents, **inclu**ding **head**ers, **lis**ts,
**an**d **co**de **blo**cks:

> ## **Th**is **i**s **a** **hea**der.
>
> 1.   **Th**is **i**s **th**e **fir**st **li**st **it**em.
> 2.   **Th**is **i**s **th**e **sec**ond **li**st **it**em.
>
> **Her**e's **so**me **exam**ple **co**de:
>
>     return shell_exec("echo $input | $markdown_script");

**An**y **dec**ent **te**xt **edi**tor **sho**uld **ma**ke **ema**il-**sty**le **quot**ing **ea**sy. **Fo**r
**exam**ple, **wi**th **BBE**dit, **yo**u **ca**n **ma**ke **a** **selec**tion **an**d **cho**ose **Incr**ease
**Quo**te **Lev**el **fr**om **th**e **Te**xt **me**nu.


### **Lis**ts

**Mark**down **supp**orts **orde**red (**numb**ered) **an**d **unord**ered (**bull**eted) **lis**ts.

**Unord**ered **lis**ts **us**e **aster**isks, **plu**ses, **an**d **hyph**ens -- **interch**angably
-- **a**s **li**st **mark**ers:

*   **Re**d
*   **Gre**en
*   **Bl**ue

**i**s **equiv**alent **t**o:

+   **Re**d
+   **Gre**en
+   **Bl**ue

**an**d:

-   **Re**d
-   **Gre**en
-   **Bl**ue

**Orde**red **lis**ts **us**e **numb**ers **foll**owed **b**y **peri**ods:

1.  **Bi**rd
2.  **McH**ale
3.  **Par**ish

**It**'s **impor**tant **t**o **no**te **th**at **th**e **act**ual **numb**ers **yo**u **us**e **t**o **ma**rk **th**e
**li**st **ha**ve **n**o **eff**ect **o**n **th**e **HT**ML **out**put **Mark**down **prod**uces. **Th**e **HT**ML
**Mark**down **prod**uces **fr**om **th**e **abo**ve **li**st **i**s:

**I**f **yo**u **inst**ead **wro**te **th**e **li**st **i**n **Mark**down **li**ke **th**is:

1.  **Bi**rd
1.  **McH**ale
1.  **Par**ish

**o**r **ev**en:

3. **Bi**rd
1. **McH**ale
8. **Par**ish

**you**'d **ge**t **th**e **exa**ct **sa**me **HT**ML **out**put. **Th**e **poi**nt **i**s, **i**f **yo**u **wa**nt **t**o,
**yo**u **ca**n **us**e **ordi**nal **numb**ers **i**n **yo**ur **orde**red **Mark**down **lis**ts, **s**o **th**at
**th**e **numb**ers **i**n **yo**ur **sou**rce **mat**ch **th**e **numb**ers **i**n **yo**ur **publi**shed **HT**ML.
**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o.

**T**o **ma**ke **lis**ts **lo**ok **ni**ce, **yo**u **ca**n **wr**ap **ite**ms **wi**th **hang**ing **inde**nts:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
    **Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
    **vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
    **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Bu**t **i**f **yo**u **wa**nt **t**o **b**e **la**zy, **yo**u **don**'t **ha**ve **t**o:

*   **Lor**em **ips**um **dol**or **si**t **am**et, **consec**tetuer **adipi**scing **el**it.
**Aliq**uam **hendr**erit **m**i **posu**ere **lec**tus. **Vesti**bulum **en**im **wi**si,
**vive**rra **ne**c, **fring**illa **i**n, **laor**eet **vit**ae, **ris**us.
*   **Don**ec **si**t **am**et **ni**sl. **Aliq**uam **sem**per **ips**um **si**t **am**et **vel**it.
**Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**Li**st **ite**ms **ma**y **cons**ist **o**f **mult**iple **parag**raphs. **Ea**ch **subse**quent
**parag**raph **i**n **a** **li**st **it**em **mu**st **b**e **inde**nted **b**y **eit**her 4 **spa**ces
**o**r **on**e **ta**b:

1.  **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs. **Lor**em **ips**um **dol**or
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  **Suspen**disse **i**d **se**m **consec**tetuer **lib**ero **luc**tus **adipi**scing.

**I**t **loo**ks **ni**ce **i**f **yo**u **ind**ent **eve**ry **li**ne **o**f **th**e **subse**quent
**parag**raphs, **bu**t **he**re **aga**in, **Mark**down **wi**ll **all**ow **yo**u **t**o **b**e
**la**zy:

*   **Th**is **i**s **a** **li**st **it**em **wi**th **tw**o **parag**raphs.

    **Th**is **i**s **th**e **sec**ond **parag**raph **i**n **th**e **li**st **it**em. **You**'re
**on**ly **requ**ired **t**o **ind**ent **th**e **fir**st **li**ne. **Lor**em **ips**um **dol**or
**si**t **am**et, **consec**tetuer **adipi**scing **el**it.

*   **Anot**her **it**em **i**n **th**e **sa**me **li**st.

**T**o **pu**t **a** **block**quote **wit**hin **a** **li**st **it**em, **th**e **blockq**uote's `>`
**delim**iters **ne**ed **t**o **b**e **inde**nted:

*   **A** **li**st **it**em **wi**th **a** **block**quote:

    > **Th**is **i**s **a** **block**quote
    > **ins**ide **a** **li**st **it**em.

**T**o **pu**t **a** **co**de **blo**ck **wit**hin **a** **li**st **it**em, **th**e **co**de **blo**ck **nee**ds
**t**o **b**e **inde**nted ***twi**ce* -- 8 **spa**ces **o**r **tw**o **ta**bs:

*   **A** **li**st **it**em **wi**th **a** **co**de **blo**ck:

        <code goes here>

### **Co**de **Blo**cks

**Pr**e-**forma**tted **co**de **blo**cks **ar**e **us**ed **fo**r **writ**ing **abo**ut **progra**mming **o**r
**mar**kup **sou**rce **co**de. **Rat**her **th**an **form**ing **nor**mal **parag**raphs, **th**e **lin**es
**o**f **a** **co**de **blo**ck **ar**e **interp**reted **liter**ally. **Mark**down **wra**ps **a** **co**de **blo**ck
**i**n **bo**th `<pre>` **an**d `<code>` **ta**gs.

**T**o **prod**uce **a** **co**de **blo**ck **i**n **Mark**down, **sim**ply **ind**ent **eve**ry **li**ne **o**f **th**e
**blo**ck **b**y **a**t **lea**st 4 **spa**ces **o**r 1 **ta**b.

**Th**is **i**s **a** **nor**mal **parag**raph:

    This is a code block.

**He**re **i**s **a**n **exam**ple **o**f **AppleS**cript:

    tell application "Foo"
        beep
    end tell

**A** **co**de **blo**ck **conti**nues **unt**il **i**t **reac**hes **a** **li**ne **th**at **i**s **no**t **inde**nted
(**o**r **th**e **en**d **o**f **th**e **arti**cle).

**Wit**hin **a** **co**de **blo**ck, **amper**sands (`&`) **an**d **ang**le **brac**kets (`<` **an**d `>`)
**ar**e **automat**ically **conve**rted **in**to **HT**ML **enti**ties. **Th**is **mak**es **i**t **ve**ry
**ea**sy **t**o **incl**ude **exam**ple **HT**ML **sou**rce **co**de **usi**ng **Mark**down -- **ju**st **pas**te
**i**t **an**d **ind**ent **i**t, **an**d **Mark**down **wi**ll **han**dle **th**e **has**sle **o**f **enco**ding **th**e
**amper**sands **an**d **ang**le **brac**kets. **Fo**r **exam**ple, **th**is:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

**Regu**lar **Mark**down **syn**tax **i**s **no**t **proce**ssed **wit**hin **co**de **blo**cks. **E**.**g**.,
**aster**isks **ar**e **ju**st **lite**ral **aster**isks **wit**hin **a** **co**de **blo**ck. **Th**is **mea**ns
**it**'s **al**so **ea**sy **t**o **us**e **Mark**down **t**o **wri**te **abo**ut **Markd**own's **ow**n **syn**tax.

```
tell application "Foo"
    beep
end tell
```

## **Sp**an **Elem**ents

### **Lin**ks

**Mark**down **supp**orts **tw**o **sty**le **o**f **lin**ks: ***inl**ine* **an**d ***refer**ence*.

**I**n **bo**th **sty**les, **th**e **li**nk **te**xt **i**s **delim**ited **b**y [**squ**are **brac**kets].

**T**o **cre**ate **a**n **inl**ine **li**nk, **us**e **a** **se**t **o**f **regu**lar **parent**heses **immedi**ately
**aft**er **th**e **li**nk **tex**t's **clos**ing **squ**are **brac**ket. **Ins**ide **th**e **parent**heses,
**pu**t **th**e **UR**L **whe**re **yo**u **wa**nt **th**e **li**nk **t**o **poi**nt, **alo**ng **wi**th **a**n ***opti**onal*
**tit**le **fo**r **th**e **li**nk, **surro**unded **i**n **quo**tes. **Fo**r **exam**ple:

**Th**is **i**s [**a**n **exam**ple](http://example.com/) **inl**ine **li**nk.

[**Th**is **li**nk](http://example.net/) **ha**s **n**o **tit**le **attri**bute.

### **Emph**asis

**Mark**down **tre**ats **aster**isks (`*`) **an**d **unders**cores (`_`) **a**s **indic**ators **o**f
**emph**asis. **Te**xt **wrap**ped **wi**th **on**e `*` **o**r `_` **wi**ll **b**e **wrap**ped **wi**th **a**n
**HT**ML `<em>` **ta**g; **dou**ble `*`'s **o**r `_`'s **wi**ll **b**e **wrap**ped **wi**th **a**n **HT**ML
`<strong>` **ta**g. **E**.**g**., **th**is **inp**ut:

***sin**gle **aster**isks*

_single underscores_

**double asterisks**

__double underscores__

### **Co**de

**T**o **indi**cate **a** **sp**an **o**f **co**de, **wr**ap **i**t **wi**th **back**tick **quo**tes (`` ` ``).
**Unl**ike **a** **pr**e-**forma**tted **co**de **blo**ck, **a** **co**de **sp**an **indic**ates **co**de **wit**hin **a**
**nor**mal **parag**raph. **Fo**r **exam**ple:

**Us**e **th**e `printf()` **func**