<div class="problem-statement"><div class="header"><h1 class="title">C. Надпись на табло</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
<p>
    Вы получили доступ к одной из камер наблюдения в особо секретной организации. В зоне видимости камеры находится табло, с которого вы постоянно считываете информацию. Теперь вам нужно написать программу, которая по состоянию табло определяет, какая буква изображена на нём в данный момент.

Табло представляет собой квадратную таблицу, разбитую на n×n равных квадратных светодиодов. Каждый диод либо включён, либо выключен. Введём систему координат, направив ось OX вправо, а ось OY вверх, приняв сторону диода равной 1.

На табло могут быть изображены только следующие буквы:

<li><strong>I</strong>&nbsp — прямоугольник из горящих диодов.</li>
<li><strong>O</strong>&nbsp — прямоугольник из горящих диодов с углами (x₁, y₁) и (x₂, y₂), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x₃, y₃) и (x₄, y₄). При этом границы выключенного прямоугольника не должны касаться внешнего, то есть x₁ < x₃ < x₄ < x₂ и y₁ < y₃ < y₄ < y₂.</li>
<li><strong>C</strong>&nbsp — прямоугольник из горящих диодов с углами (x₁, y₁) и (x₂, y₂), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x₃, y₃) и (x₄, y₄). Правая граница выключенного прямоугольника находится на правой границе внешнего прямоугольника, то есть x₁ < x₃ < x₄ = x₂ и y₁ < y₃ < y₄ < y₂.</li>
</p> <p><img src="https://contest.yandex.ru/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..u5xkMWoMtyI97UjS.iYn_69cMruJEtyVytTHxPFXrtK3b3ZDbjo8tZ2_ETrlG8HXcBRketRCz6yQDpFbg6nYfjVB_nlYP3m0IVQLH2aLHRg.O0tFoGc_6C6OUk-VD8Qr1w" alt="image"></p>
<p>
<li><strong>L</strong>&nbsp — прямоугольник из горящих диодов с углами (x₁, y₁) и (x₂, y₂), внутри которого есть прямоугольник из выключенных диодов с координатами углов (x₃, y₃) и (x₄, y₄). При этом правые верхние углы выключенного и внешнего прямоугольника совпадают: x₁ < x₃ < x₄ = x₂ и y₁ < y₃ < y₄ = y₂. </li>
<li><strong>H</strong>&nbsp — прямоугольник из горящих диодов с углами (x₁, y₁) и (x₂, y₂), внутри которого находятся 2 прямоугольника из выключенных диодов с углами (x₃, y₃), (x₄, y₄) у первого и (x₅, y₅), (x₆, y₆) у второго. Выключенные прямоугольники должны иметь одинаковую ширину, находиться строго один под другим, один должен касаться верхней стороны, а другой — нижней стороны внешнего прямоугольника: x₁ < x₃ = x₅ < x₄ = x₆ < x₂ и y₁ = y₃ < y₄ < y₅ < y₆ = y₂. </li>
</p> <p><img src="https://contest.yandex.ru/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..TTuWUFL7XVBGvmzG.Gn5nsY5fEadhVd_H_BFJJXstG9v9i4zuJjejZZanTBm_-2p5zGwNUXOiDOCIo33X-wYBJyO33HaqERVNaHcNe0TTSQ.couqjh5liAdANNT2-dGPyg" alt="image"></p>
<p>
<li><strong>P</strong>&nbsp — прямоугольник из горящих диодов с углами (x₁, y₁) и (x₂, y₂), внутри которого находятся 2 прямоугольника из выключенных диодов с углами (x₃, y₃), (x₄, y₄) у первого и (x₅, y₅), (x₆, y₆) у второго. Правый нижний угол первого выключенного прямоугольника должен совпадать с правым нижним углом внешнего, а другой выключенный должен находиться строго выше и не касаться границ. Левые границы двух выключенных прямоугольников должны совпадать: x₁ < x₃ = x₅ < x₆ < x₄ = x₂ и y₁ = y₃ < y₄ < y₅ < y₆ < y₂.</li>
</p> <p><img src="https://contest.yandex.ru/testsys/statement-file?hash=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..G5STebcZpPtbHJ8O.OJh24utcIZlDsfx30DiER7tTiLBFVkgd3DdF4dA0ZYNPCorDvW_JGaZNz4axG2zDA1CArupqzK2gaOpkQZnsuLR1gA.ViNM6tnn06L5XGGQJ-FRGw" alt="image"></p></li> 
<p> 
<li> Любое другое состояние табло считается буквой <strong>X</strong>. </li>
</p></div><h2>Формат ввода</h2><div class="input-specification"><p>
В первой строке — одно число n (1 ≤ n ≤ 10) — сторона табло.

В следующих n строках — строки длины n из символов "." и "#": "." обозначает выключенный квадратный диод, а "#" — горящий.
</p></div><h2>Формат вывода</h2><div class="output-specification"><p>
    Программа должна вывести единственный символ: если таблица соответствует одной из букв <strong>I</strong>, <strong>O</strong>, <strong>C</strong>, <strong>L</strong>, <strong>H</strong>, <strong>P</strong>, выведите её (все буквы — английские). Если же таблица не соответствует ни одному из условий, выведите <strong>X</strong>.
</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
.##.
.##.
.##.
....
</pre></td><td><pre><strong>I</strong>
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>5
#...#
.#.#.
..#..
.#.#.
#...#
</pre></td><td><pre><strong>X</strong>
</pre></td></tr></tbody></table>
