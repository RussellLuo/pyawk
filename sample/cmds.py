# this is a sample
cmds = [

'''BEGIN { print("[ALL]") }
   { print($0) }',
   END { print("-"*10) }''',

'''BEGIN { OFS=" && "; print("[CN]") }
   $3 == "CN" { print($1, NR) }
   END { print("-"*10) }''',

'''BEGIN { count = 0; print("[MALE]") }
   $2/^male/ { count += 1; print($1) }
   END { print("|There are *%d* lines matched|" % count); print("-"*10) }''',

'''
BEGIN { OFS = " "; print("[AGE]") }
{
if $4 <= 10:
    print("%-10s%s" % ($1, "young"))
elif $4 <= 40:
    print("%-10s%s" % ($1, "middle"))
else:
    print("%-10s%s" % ($1, "old"))
}
END { print("-"*10) }
''',

]
