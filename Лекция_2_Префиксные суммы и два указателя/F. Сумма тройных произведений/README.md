<div class="problem-statement"><div class="header"><h1 class="title">F. Сумма тройных произведений</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>2&nbsp;секунды</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>512Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend"><p>Задана последовательность из <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>. Найдите число</p> 
<p><span class="math display"><span class="katex-display"><span class="katex"><span class="katex-mathml">
     <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
      <semantics>
       <mrow>
        <munder>
         <mo>
          ∑
         </mo>
         <mrow>
          <mn>
           1
          </mn>
          <mo>
           ≤
          </mo>
          <mi>
           i
          </mi>
          <mo>
           &lt;
          </mo>
          <mi>
           j
          </mi>
          <mo>
           &lt;
          </mo>
          <mi>
           k
          </mi>
          <mo>
           ≤
          </mo>
          <mi>
           n
          </mi>
         </mrow>
        </munder>
        <msub>
         <mi>
          a
         </mi>
         <mi>
          i
         </mi>
        </msub>
        <mo>
         ⋅
        </mo>
        <msub>
         <mi>
          a
         </mi>
         <mi>
          j
         </mi>
        </msub>
        <mo>
         ⋅
        </mo>
        <msub>
         <mi>
          a
         </mi>
         <mi>
          k
         </mi>
        </msub>
       </mrow>
       <annotation encoding="application/x-tex">
        \sum\limits_{1 \le i &lt; j &lt; k \le n} a_i \cdot a_j \cdot a_k
       </annotation>
      </semantics>
     </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:2.4882em;vertical-align:-1.4382em;"></span><span class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.05em;"><span style="top:-1.8479em;margin-left:0em;"><span class="pstrut" style="height:3.05em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">1</span><span class="mrel mtight">≤</span><span class="mord mathnormal mtight">i</span><span class="mrel mtight">&lt;</span><span class="mord mathnormal mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">&lt;</span><span class="mord mathnormal mtight" style="margin-right:0.03148em;">k</span><span class="mrel mtight">≤</span><span class="mord mathnormal mtight">n</span></span></span></span><span style="top:-3.05em;"><span class="pstrut" style="height:3.05em;"></span><span><span class="mop op-symbol large-op">∑</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:1.4382em;"><span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.7306em;vertical-align:-0.2861em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.05724em;">j</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2861em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">⋅</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p>Поскольку число может получиться слишком большим, требуется посчитать его по модулю <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        000
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        000
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        007
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1\,000\,000\,007
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">000</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">000</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">007</span></span></span></span></span>.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>В первой строке дано одно целое число <span class="math inline"><span class="katex"><span class="katex-mathml">
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
        3
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
         6
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       3 \le n \le 10^6
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">3</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7719em;vertical-align:-0.136em;"></span><span class="mord mathnormal">n</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>).</p> 
<p>Во второй строке даны <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span> целых чисел <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span> (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        0
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
         6
        </mn>
       </msup>
      </mrow>
      <annotation encoding="application/x-tex">
       0 \le a_i \le 10^6
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7804em;vertical-align:-0.136em;"></span><span class="mord">0</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.786em;vertical-align:-0.15em;"></span><span class="mord"><span class="mord mathnormal">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3117em;"><span style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">6</span></span></span></span></span></span></span></span></span></span></span></span>).</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Выведите требуемое число по модулю <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mn>
        1
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        000
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        000
       </mn>
       <mtext>
         
       </mtext>
       <mn>
        007
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       1\,000\,000\,007
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">000</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">000</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">007</span></span></span></span></span>.</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>3
1 2 3
</pre></td><td><pre>6
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
0 5 6 7
</pre></td><td><pre>210
</pre></td></tr></tbody></table>