<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Сумма номеров</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"> Вася очень любит везде искать своё счастливое число <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>.
      Каждый день он ходит в школу по улице, вдоль которой припарковано <!--l. 47--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> машин. Он заинтересовался вопросом, сколько существует наборов
      машин, стоящих подряд на местах с <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi></math>
      до <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math>,
      что сумма их номеров равна <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>.
      Помогите Васе узнать ответ на его вопрос. <!--l. 49-->
      <p style="text-indent: 0em;">Например, если число <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi>
      <mo>=</mo> <mn>5</mn></math>, <!--l. 49--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi>
      <mo>=</mo> <mn>1</mn><mn>7</mn></math>, а номера машин равны 17, 7, 10, 7, 10, то существует 4 набора машин: <!--l. 51-->
      </p><p style="text-indent: 0em;">17 (<!--l. 51--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi>
      <mo>=</mo> <mn>1</mn><mo>,</mo><mi>R</mi> <mo>=</mo> <mn>1</mn></math>), <!--l. 53-->
      </p><p style="text-indent: 0em;">7, 10 (<!--l. 53--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi>
      <mo>=</mo> <mn>2</mn><mo>,</mo><mi>R</mi> <mo>=</mo> <mn>3</mn></math>), <!--l. 55-->
      </p><p style="text-indent: 0em;">10, 7 (<!--l. 55--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi>
      <mo>=</mo> <mn>3</mn><mo>,</mo><mi>R</mi> <mo>=</mo> <mn>4</mn></math>), <!--l. 57-->
      </p><p style="text-indent: 0em;">7, 10 (<!--l. 57--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi>
      <mo>=</mo> <mn>4</mn><mo>,</mo><mi>R</mi> <mo>=</mo> <mn>5</mn></math>) </p>
      <p></p>
      <p></p>
      <p></p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных задаются числа <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      и <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math>
      (<!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>N</mi> <mo>≤</mo> <mn>1</mn><mn>0</mn><mn>0</mn><mspace width="0.3em"><mn>0</mn><mn>0</mn><mn>0</mn></mspace></math>,
      <!--l. 60--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>K</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>). <!--l. 62-->
      <p style="text-indent: 0em;">Во второй строке содержится <!--l. 62--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      чисел, задающих номера машин. Номера машин могут принимать значения от <!--l. 62--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math> до <!--l. 62--><math display="inline" style="text-indent:
      0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn><mn>9</mn><mn>9</mn></math> включительно. </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Необходимо вывести одно число&nbsp;— количество наборов. </div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 17
17 7 10 7 10
</pre></td>
            <td><pre>4
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 10
1 2 3 4 1
</pre></td>
            <td><pre>2
</pre></td>
         </tr>
      </tbody>
   </table>