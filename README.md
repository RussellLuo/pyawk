PyAWK
=====

A simple variant of AWK in Python.

1| Motivation
-------------

Keep **simple**, **wonderful** and **the most frequently used** features in `awk`, while replacing the **complicated** and **ambiguous** syntax with `Python`. As a result, we can get the power of both `Python` and `awk` by using `pyawk`, a pythonic awk.

2| pyawk vs awk
---------------

+ **usage**

    pyawk:
    
        pyawk [option] 'pattern { action }' file
    
    awk:
    
        awk [option] 'pattern { action }' file1 file2 ...

+ **option**

    pyawk        | awk                    | Remarks
    ------------ | ---------------------- | -------
    -F fs        | -F fs                  |
    -f progfile  | -f progfile            | (1)
    -v (verbose) | -v var=val             |
    ×            | other options in `awk` |

    (1) In `pyawk`, "progfile" is actually a Python module, in which all commands are included in a list called `cmds`. While "progfile" is just a normal text file in `awk`.

+ **pattern**

    pyawk                             | awk                               | Remarks
    --------------------------------- | --------------------------------- | -------
    /regex/ <=> $0/regex/             | /regex/ <=> $0 ~ /regex/          | (1)
    $1/regex/                         | $1 ~ /regex/                      | (1)
    $1!/regex/                        | $1 !~ /regex/                     | (1)
    all valid expressions in `Python` | all valid expressions in `awk`    | (2)
    begpat, endpat                    | begpat, endpat                    | (3)
    BEGIN { action }                  | BEGIN { action }                  | (4)
    END { action }                    | END { action }                    | (4)
    no pattern <=> match every record | no pattern <=> match every record | (5)
    ×                                 | other patterns in `awk`           |

    (1) regular expression

    (2) expression

    (3) begpat, endpat

    (4) BEGIN/END

    (5) empty

+ **action**

    pyawk                            | awk
    -------------------------------- | -------------------------------
    all valid statements in `Python` | all valid statements in `awk`
    print($1, $2, $3)                | print $1, $2, $3
    no action <=> `print($0)`        | no action <=> `print $0`
    `print` (×, must be `print($0)`) | `print` (√, <=> `print $0`)
    ×                                | variables used before defined

+ **built-in variable**

    pyawk | awk                               | Remarks
    ----- | --------------------------------- | -----------------------
    NR    | NR                                | Number of Records
    NF    | NF                                | Number of Fields
    FS    | FS                                | input Field Separator
    RS    | RS                                | input Record Separator
    OFS   | OFS                               | Output Field Separator
    ORS   | ORS                               | Output Record Separator
    ×     | other built-in variables in `awk` |

3| Usage
--------

### 1) Install

    sudo python setup.py install

### 2) Uninstall

    sudo python setup.py uninstall

### 3) Examples

See help message of command `pyawk`:

    pyawk 'END { print(NR) }' /etc/passwd
    echo -e 'python .py\nperl .pl\nshell .sh' | pyawk '$2!/pl/{ print($1) }'
    ps aux | pyawk 'BEGIN { print("USER|PID|COMMAND") }; $2 == 10, $2 == 50 { print($1, $2, $11) }'

See directory `sample`:

    pyawk -f sample.cmds sample/data.txt

