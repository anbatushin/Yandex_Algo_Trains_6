<div class="problem-statement"><div class="header"><h1 class="title">I. Автоматизированный склад*</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend"><p>Склад представляет собой набор одинаковых квадратов, вокруг которых расположены проезды. В углах каждого из квадратов расположены перекрестки, образованные из пересекающихся под прямым углом проездов.</p> 
<p>По складу движутся роверы и при проезде перекрестков они руководствуются следующими правилами:</p> 
<ul> 
 <li><p>На перекрестке неравнозначных дорог ровер, движущийся по второстепенной дороге, должен уступить дорогу роверу, приближающимся по главной.</p></li> 
 <li><p>Если главная дорога на перекрестке меняет направление, роверы, движущиеся по главной дороге, должны руководствоваться между собой правилами проезда перекрестков равнозначных дорог.</p></li> 
 <li><p>На перекрестке равнозначных дорог ровер обязан уступить дорогу транспортным средствам, приближающимся справа.</p></li> 
</ul> 
<p>Для тестирования был выбран перекресток, для которого необходимо определить в каком порядке его проедут <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> роверов, подъезжающих к перекрестку с каждой из четырех сторон в заданные моменты времени. Стороны обозначены номерами 1, 2, 3 и 4, если перечислять по часовой стрелке. Известно, что за единицу времени с каждой из сторон перекрестка приезжает не более одного ровера, а все роверы соблюдают правила и не обгоняют друг-друга. Поскольку это только начало тестирования, все роверы хотят проехать перекресток прямо. Роверы, приближающиеся со сторон <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        a
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       a
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">a</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        b
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       b
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal">b</span></span></span></span></span> находятся на главной дороге, остальные&nbsp;— на второстепенной. На проезд перекрестка ровер тратит одну единицу времени.</p> 
<p>Таким образом, ровер проезжает перекресток только если:</p> 
<ul> 
 <li><p>нет роверов, которые находятся перед этим ровером в очереди к перекрестку,</p></li> 
 <li><p>нет роверов, которым нужно уступить дорогу</p></li> 
</ul> 
<p>Если два ровера, стоящие первыми в очереди на проезд перекрестка не должны уступать друг другу дорогу, то они проедут перекресток одновременно.</p> 
<p>Определите, в каком порядке роверы проедут перекресток.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>Первая строка входного файла содержит одно целое число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <mi>
        N
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        100
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le N \le 100
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8193em;vertical-align:-0.136em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">100</span></span></span></span></span>)&nbsp;— количество роверов. Вторая строка содержит числа <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        a
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       a
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">a</span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        b
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       b
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal">b</span></span></span></span></span>&nbsp;— стороны перекрестка, составляющие главную дорогу (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <mi>
        a
       </mi>
       <mo separator="true">
        ,
       </mo>
       <mi>
        b
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        4
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le a,b \le 4
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">4</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        a
       </mi>
       <mo mathvariant="normal">
        ≠
       </mo>
       <mi>
        b
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       a \ne b
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal">a</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="inner"><span class="mord"><span class="mrel"></span></span></span><span class="fix"></span></span></span></span></span><span class="mrel">=</span></span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal">b</span></span></span></span></span>).</p> 
<p>Каждая из следующих <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> строк содержит описание ровера, состоящее из двух целых чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         d
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       d_i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8444em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         t
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       t_i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7651em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <msub>
        <mi>
         d
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mo>
        ≤
       </mo>
       <mn>
        4
       </mn>
       <mo separator="true">
        ,
       </mo>
       <mn>
        1
       </mn>
       <mo>
        ≤
       </mo>
       <msub>
        <mi>
         t
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mo>
        ≤
       </mo>
       <mn>
        100
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le d_i \le 4, 1 \le t_i \le 100
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8444em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">d</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8389em;vertical-align:-0.1944em;"></span><span class="mord">4</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.786em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">t</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">100</span></span></span></span></span>)&nbsp;— направление и время приезда <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        i
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-ого ровера.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>В выходной файл выведите <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> целых чисел по одному на строке. <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        i
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-ая строка должна содержать время, в которое <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        i
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6595em;"></span><span class="mord mathnormal">i</span></span></span></span></span>-ый ровер проедет перекресток.</p> 
<p>Роверы занумерованы в порядке появления во входном файле.</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
1 3
1 1
3 1
2 1
2 2
</pre></td><td><pre>1
1
2
3
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
1 2
1 1
2 1
3 1
4 1
</pre></td><td><pre>1
2
3
4
</pre></td></tr></tbody></table><h3>Пример 3</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>1
1 4
1 1
</pre></td><td><pre>1
</pre></td></tr></tbody></table>