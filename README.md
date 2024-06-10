# sivt-json-client-test

- mějme server
- vystavené kolekce:
  - `/zbozi`: všechno zboží, umí GET, POST
  - `/zbozi/{id}`: detail konkrétní položky, umí GET, PUT, DELETE

- Insomnia:
  - jaký formát má seznam zboží?: popište hrubou kostru
  - jak se liší položka v seznamu od detailu konkrétní položky (1 rozdíl)?
  - jak odpovídá server na pokus smazat neexistující položku?
  - jak odpovídá server na úspěšné vytvoření nové položky?
  - jak odpovídá server na pokus vytvořit novou položku s již existujícím ID?
- odpovídejte do Google classroom

- Python:
  - dopište třídu Klient tak, aby správně fungoval příkladový kód v metodě `test()`
  - tělo metody `test()` neupravujte
  - dopište ji tak, aby vám mypy nehlásilo žádné typové chyby
  - pokuste se správně ošetřit chybové návratové kódy
