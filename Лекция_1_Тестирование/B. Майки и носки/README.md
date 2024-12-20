<div class="problem-statement"><div class="header"><h1 class="title">B. Майки и носки</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
    Как известно, осенью и зимой светает поздно, и так хочется утром ещё хоть немного поспать, а не идти в школу! Некоторые школьники готовы даже одеваться, не открывая глаз, лишь бы отложить момент пробуждения. Вот и Саша решил, что майку и носки он вполне может вытащить из шкафа на ощупь с закрытыми глазами и только потом включить свет и одеться. В шкафу у Саши есть два ящика. В одном из них лежит A синих и B красных маек, в другом — C синих и D красных пар носков. Саша хочет, чтобы и майка, и носки были одного цвета. Он вслепую вытаскивает M маек и N пар носков. В первое же утро Саша задумался, какое минимальное суммарное количество предметов одежды (M+N) он должен вытащить, чтобы среди них гарантированно оказались майка и носки одного цвета. Какого именно цвета окажутся предметы одежды, для Саши совершенно неважно.
</p></div><h2>Формат ввода</h2><div class="input-specification"><p>
   На вход программе подаются четыре целых неотрицательных числа A, B, C, D, записанных в отдельных строках:
A — количество синих маек,
B — количество красных маек,
C — количество синих носков,
D — количество красных носков.
Все числа не превосходят 10⁹. Гарантируется, что в шкафу есть одноцветный комплект из майки и носков.
</p></div><h2>Формат вывода</h2><div class="output-specification"><p>
    Программа должна вывести два числа: количество маек M и количество пар носков N, которые должен взять Саша. Необходимо, чтобы среди M маек и N пар носков обязательно нашлась одноцветная пара, при этом сумма M + N должна быть минимальной.
</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>6
2
7
3
</pre></td><td><pre>3 4
</pre></td></tr></tbody></table><h2>
    Примечания</h2><div class="notes"> <p>
        В примере из условия в шкафу лежит A = 6 синих маек и B = 2 красных маек. Если взять 3 майки, то среди них обязательно найдётся синяя. В другом ящике лежит C = 7 пар синих носков и D = 3 пары красных носков. Если взять 4 пары, то среди них обязательно будет пара синих носков. Поэтому если взять вслепую 3 майки и 4 пары носков, то среди них обязательно найдётся одноцветный (синий) комплект из майки и носков.
    </p></div>
