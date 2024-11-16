<div class="problem-statement"><div class="header"><h1 class="title">E. Удаление медиан</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>2&nbsp;секунды</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend"><p>Задана последовательность чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       a_i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> длиной <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>. Из него необходимо последовательно удалять медианы.</p> 
<p>Медиана в этой задаче определяются следующим образом:</p> 
<ul> 
 <li><p>Если количество чисел в последовательности нечетно, то медиана&nbsp;— число, стоящее точно в середине упорядоченной по возрастанию последовательности.</p></li> 
 <li><p>Если количество чисел в последовательности чётно, то медианой последовательности является:</p> 
  <ul> 
   <li><p>Меньшее из двух стоящих посередине чисел упорядоченной по возрастанию последовательности, если два средних различны.</p></li> 
   <li><p>Любое из двух стоящих посередине чисел упорядоченной по возрастанию последовательности, если два средних равны.</p></li> 
  </ul></li> 
</ul> 
<p>Определите в каком порядке будут удалены элементы последовательности.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>В первой строке дано одно натуральное число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>&nbsp;— количество элементов последовательности (<span class="math inline"><span class="katex"><span class="katex-mathml">
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
        n
       </mi>
       <mo>
        ≤
       </mo>
       <mn>
        1
       </mn>
       <msup>
        <mn>
         0
        </mn>
        <mn>
         5
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le n \le 10^5
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">5</span></span></span></span></span></span></span></span></span></span></span></span>).</p> 
<p>Во второй строке содержатся <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> натуральных чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <msub>
        <mi>
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
      </mrow>
      <annotation encoding="application/x-tex">
       a_i
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>&nbsp;— элементы последовательности (<span class="math inline"><span class="katex"><span class="katex-mathml">
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
         a
        </mi>
        <mi>
         i
        </mi>
       </msub>
       <mo>
        ≤
       </mo>
       <mn>
        1
       </mn>
       <msup>
        <mn>
         0
        </mn>
        <mn>
         9
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le a_i \le 10^9
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.786em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span></span></span></span>).</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Выведите <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        n
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       n
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> чисел&nbsp;— порядок удаления чисел из последовательности.</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>3
19 3 8
</pre></td><td><pre>8 3 19 
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
1 2 4 2
</pre></td><td><pre>2 2 1 4 
</pre></td></tr></tbody></table>