Projekt wykonywany samodzielnie o nazwie "Steady as she goes!". Dokładny opis znajduje się w pliku 'sprawozdanie'. Do znajdywania najkrótszej drogi wykorzystano aglorytm 'A*'. Polecenie brzmiało:

Kapitan planuję przepłynąć akwen reprezentowany przez kwadrat wielkości NxN. Problemem jest jednak fakt że akwen znajduje się w płytkim rejonie, w związku z czym wasz statek może przepływać tylko przez pola o głębokości większej niż jego zanurzenie. Jako wprawny nawigator doskonale wiesz co musisz w tym momencie zrobić.
Korzystając z dokładnej locji (mapy obrazującej wysokość dna), pomóż kapitanowi zaplanować trasę (dowolną/najkrótszą) z górnego lewego pola mapy [0,0] do dolnego prawego [n-1,n-1]. Wynikową trasę nanieś na mapę i przedstaw kapitanowi.
Przygotuj interfejs graficzny który umożliwi komunikację z programem. Interfejs powinien umożliwić stworzenie locji w formie mapy NxN w którą użytkownik będzie mógł wpisywać wysokość terenu w m.n.p.m. Interfejs powininen w czytelny sposób obrazować głębokości i wysokości (jeżeli teren jest powyżej 0 powinien zostać odpowiednio zaznaczony jako ląd, poniżej 0 jako morze). Głębokość i wysokość terenu powinna mieć wpływ na wizualizację.
Wejście:
    Macierz NxN z liczbami (float) opisującymi teren, zanurzenie fregaty
Wyjście:
    Wizualizacja najkrótszej trasy
Biblioteki:
numpy, matplotlib, Pillow
