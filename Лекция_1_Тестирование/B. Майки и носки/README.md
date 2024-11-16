<div class="problem-statement"><div class="header"><h1 class="title">B. Майки и носки</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend"><p>Как известно, осенью и зимой светает поздно, и так хочется утром ещё хоть немного поспать, а не идти в школу! Некоторые школьники готовы даже одеваться, не открывая глаз, лишь бы отложить момент пробуждения. Вот и Саша решил, что майку и носки он вполне может вытащить из шкафа на ощупь с закрытыми глазами и только потом включить свет и одеться. В шкафу у Саши есть два ящика. В одном из них лежит <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        A
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       A
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal">A</span></span></span></span></span> синих и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        B
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       B
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.05017em;">B</span></span></span></span></span> красных маек, в другом — <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        C
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       C
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span></span></span></span></span> синих и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        D
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       D
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">D</span></span></span></span></span> красных пар носков. Саша хочет, чтобы и майка, и носки были одного цвета. Он вслепую вытаскивает <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        M
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       M
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span></span></span></span></span> маек и <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> пар носков. В первое же утро Саша задумался, какое минимальное суммарное количество предметов одежды (<span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        M
       </mi>
       <mo>
        +
       </mo>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       M + N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7667em;vertical-align:-0.0833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span>) он должен вытащить, чтобы среди них гарантированно оказались майка и носки одного цвета. Какого именно цвета окажутся предметы одежды, для Саши совершенно неважно.</p></div><h2>Формат ввода</h2><div class="input-specification"><p>На вход программе подаются четыре целых неотрицательных числа <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        A
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       A
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal">A</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        B
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       B
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.05017em;">B</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        C
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       C
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span></span></span></span></span>, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        D
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       D
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">D</span></span></span></span></span>, записанных в отдельных строках: <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        A
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       A
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal">A</span></span></span></span></span> — количество синих маек, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        B
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       B
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.05017em;">B</span></span></span></span></span> — количество красных маек, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        C
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       C
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span></span></span></span></span> — количество синих носков, <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        D
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       D
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">D</span></span></span></span></span> — количество красных носков. Все числа не превосходят <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
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
       10^9
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8141em;"></span><span class="mord">1</span><span class="mord"><span class="mord">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">9</span></span></span></span></span></span></span></span></span></span></span></span>. Гарантируется, что в шкафу есть одноцветный комплект из майки и носков.</p></div><h2>Формат вывода</h2><div class="output-specification"><p>Программа должна вывести два числа: количество маек <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        M
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       M
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span></span></span></span></span> и количество пар носков <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span>, которые должен взять Саша. Необходимо, чтобы среди <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        M
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       M
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span></span></span></span></span> маек и <span class="math inline"><span class="katex"><span class="katex-mathml">
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
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> пар носков обязательно нашлась одноцветная пара, при этом сумма <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        M
       </mi>
       <mo>
        +
       </mo>
       <mi>
        N
       </mi>
      </mrow>
      <annotation encoding="application/x-tex">
       M + N
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.7667em;vertical-align:-0.0833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span></span></span></span></span> должна быть минимальной.</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>6
2
7
3
</pre></td><td><pre>3 4
</pre></td></tr></tbody></table><h2>Примечания</h2><div class="notes"><p>В примере из условия в шкафу лежит <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        A
       </mi>
       <mo>
        =
       </mo>
       <mn>
        6
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       A = 6
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal">A</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">6</span></span></span></span></span> синих маек и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        B
       </mi>
       <mo>
        =
       </mo>
       <mn>
        2
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       B = 2
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.05017em;">B</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">2</span></span></span></span></span> красных маек. Если взять 3 майки, то среди них обязательно найдётся синяя. В другом ящике лежит <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        C
       </mi>
       <mo>
        =
       </mo>
       <mn>
        7
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       C = 7
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">7</span></span></span></span></span> пар синих носков и <span class="math inline"><span class="katex"><span class="katex-mathml">
    <math xmlns="http://www.w3.org/1998/Math/MathML">
     <semantics>
      <mrow>
       <mi>
        D
       </mi>
       <mo>
        =
       </mo>
       <mn>
        3
       </mn>
      </mrow>
      <annotation encoding="application/x-tex">
       D = 3
      </annotation>
     </semantics>
    </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.6833em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">D</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.6444em;"></span><span class="mord">3</span></span></span></span></span> пары красных носков. Если взять 4 пары, то среди них обязательно будет пара синих носков. Поэтому если взять вслепую 3 майки и 4 пары носков, то среди них обязательно найдётся одноцветный (синий) комплект из майки и носков.</p></div>