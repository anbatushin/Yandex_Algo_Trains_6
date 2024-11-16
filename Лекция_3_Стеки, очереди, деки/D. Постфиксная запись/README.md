<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Постфиксная запись</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
   <div class="legend"> В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел
      A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B
      + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов
      для своего чтения. 
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *. Цифры и операции разделяются
      пробелами. В конце строки может быть произвольное количество пробелов. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Необходимо вывести значение записанного выражения. </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>8 9 + 1 7 - *
</pre></td>
            <td><pre>-102
</pre></td>
         </tr>
      </tbody>
   </table>