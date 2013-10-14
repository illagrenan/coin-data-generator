## Generátor náhodných dat pro předmět MI-PPR (Problém mincomatu)

```bash
$ python main.py -h
usage: main.py [-h] [-coin-count COIN_COUNT] [-amount-count AMOUNT_COUNT] [-max-amount MAX_AMOUNT]
```
   
### Argumenty

Argument | Typ | Popis | Výchozí hodnota
--- | --- | --- | ---
-h, --helpshow | `-` | Zobrazí nápovědu | -
-coin-count, -c | `<int>` | Kolik mincí (pozic) použít | náhodné číslo 
-amount-count, -a | `<int>` | Kolik částek generovat | náhodné číslo 
-max-amount, -a | `<int>` | Nejvyšší povolená částka | náhodné číslo 

### Ukázka použití a výstupu

```shell
$ python .\main.py -c 2 -a 7 -m 50
Namespace(amount_count=7, coin_count=2, max_amount=50)
Ulozeno do data/result.txt
```

`data/result.txt`

```
2 16 24 32 40 41 42 45
^.......................... Počet mincí (pozic)
  ^........................ První částka
     ^..................... Druhá částka
        ...
```

