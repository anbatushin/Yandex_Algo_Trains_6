<div class="problem-statement"><div class="header"><h1 class="title">H. Стек с суммой*</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend"><p>Стек с суммой должен поддерживать три операции:</p> 
<ol> 
 <li><p>Добавить число <span class="math inline"><span class="katex"><span class="katex-mathml">
      <math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mi>
          x
         </mi>
        </mrow>
        <annotation encoding="application/x-tex">
         x
        </annotation>
       </semantics>
      </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">x</span></span></span></span></span> в стек</p></li> 
 <li><p>Подсчитать и вывести сумму <span class="math inline"><span class="katex"><span class="katex-mathml">
      <math xmlns="http://www.w3.org/1998/Math/MathML">
       <semantics>
        <mrow>
         <mi>
          k
         </mi>
        </mrow>
        <annotation encoding="application/x-tex">
         k
        </annotation>
       </semantics>
      </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span> чисел находящихся на вершине стека</p></li> 
 <li><p>Удалить число из стека</p></li> 
</ol> 
<p>Реализуйте структуру данных, которая поддерживает эти операции.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>В первой строке задается количество операций со стеком <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
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
        100000
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le n \le 100000
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">100000</span></span></span></span></span>).</p> 
<p>В следующих <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> строках задаются операции со стеком. Каждая операция имеет один из трех типов:</p> 
<p><span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo>
        +
       </mo>
       <mi>
        x
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       +x
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6667em;vertical-align:-0.0833em;"></span><span class="mord">+</span><span class="mord mathnormal">x</span></span></span></span></span>&nbsp;— добавить в стек число <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        x
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       x
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">x</span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
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
        x
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
         9
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       1 \le x \le 10^9
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">x</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span></span></span></span>)</p> 
<p><span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo>
        −
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       -
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6667em;vertical-align:-0.0833em;"></span><span class="mord">−</span></span></span></span></span>&nbsp;— удалить элемент с вершины стека (гарантируется, что в этот момент стек не пуст)</p> 
<p><span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo stretchy="false">
        ?
       </mo>
       <mi>
        k
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       ?k
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mclose">?</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span>&nbsp;— подсчитать и вывести сумму <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        k
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       k
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span> элементов на вершине стека (гарантируется, что в стеке не менее <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        k
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       k
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span> элементов)</p> 
<p>Изначально стек пуст.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Для каждого запроса "<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo>
        −
       </mo>
      </mrow>
      <annotation encoding="application/x-tex">
       -
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6667em;vertical-align:-0.0833em;"></span><span class="mord">−</span></span></span></span></span>" необходимо вывести значение удаляемого из стека элементов, а для каждого запроса "<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mo stretchy="false">
        ?
       </mo>
       <mi>
        k
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       ?k
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mclose">?</span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span>"&nbsp;— сумму <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        k
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       k
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span></span></span></span></span> элементов на вершине стека.</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>7
+1
+2
+3
?2
-
-
?1
</pre></td><td><pre>5
3
2
1
</pre></td></tr></tbody></table>