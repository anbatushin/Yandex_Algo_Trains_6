<div class="problem-statement"><div class="header"><h1 class="title">I. Изучение алгоритмов*</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
    <p>
    Вася готовится к алгоритмической секции собеседования и выяснил, что ему нужно изучить n алгоритмов. Вася поверхностно изучил каждый из них и охарактеризовал i-й алгоритм двумя параметрами: aᵢ (интересность) и bᵢ (полезность).

Вася работает сисадмином на научной базе в Антарктиде и никуда не торопится. Он будет изучать по одному алгоритму в день. Если ему скучно, то он будет изучать самый интересный алгоритм (с максимальным aᵢ) из всех еще не изученных. А если у него воодушевленное настроение, то выберет для изучения самый полезный алгоритм из еще не изученных (с максимальным bᵢ).

Если есть несколько алгоритмов с максимальным интересующим Васю параметром, то он выберет тот, у которого второй параметр наибольший. Если и вторые параметры равны, то Вася выберет алгоритм с меньшим порядковым номером.

Вася — предсказуемый человек (и гордится этим), поэтому он знает свое настроение на n дней вперед. Определите, в каком порядке он изучит алгоритмы.

</div><h2>Формат ввода</h2><div class="input-specification">
<p>
В первой строке ввода дано целое число n — количество алгоритмов (1 ≤ n ≤ 10⁵).

Во второй строке через пробел перечислены n целых чисел aᵢ — значения интересности алгоритмов (1 ≤ aᵢ ≤ 10⁹). В третьей строке в том же формате даны целые числа bᵢ — значения полезности алгоритмов (1 ≤ bᵢ ≤ 10⁹).

В последней строке через пробел перечислены n целых чисел pᵢ — индикаторы настроения Васи в ближайшие n дней. Если pᵢ = 1, Вася выберет алгоритм с максимальной полезностью (максимальным bᵢ), иначе pᵢ = 0, и Вася выберет самый интересный из доступных алгоритмов (с максимальным aᵢ).

</p>
</div><h2>Формат вывода</h2><div class="output-specification">
<p>
Выведите n различных целых чисел от 1 до n, разделенных пробелами; i-е число должно быть равно номеру алгоритма, который Вася будет изучать в i-й день.
</p>

</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>5
1 2 3 4 5
5 4 3 2 1
1 0 1 0 0
</pre></td><td><pre>1 5 2 4 3 </pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>6
3 10 6 2 10 1
3 5 10 7 5 9
0 0 1 1 0 1
</pre></td><td><pre>2 5 3 6 1 4 </pre></td></tr></tbody></table>
