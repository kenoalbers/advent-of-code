# [Advent of Code :christmas_tree:](https://adventofcode.com)
Exploring new languages, features, and packages while learning and experimenting with different programming paradigms,
patterns, and approaches.

View the description for highlights of the day, unique features, programming styles, notable approaches, 
and distinctive characteristics demonstrated in the solution.

> **Note:**  
> No files share any contents. Challenge part 1 and 2 are independent of one another and code is copied for part 2.

<details>
<summary>Year 2024</summary>
<br/>
The year of the :snake: Python :snake:
<br/>
<br/>

> **Folder structure:**
> - \<year number\>
>  - \<day number\>
>    - assets
>      - input.txt (individual challenge input)
>      - input_demo.txt (example input)
>      - input_demo_2.txt (if available)
>    - 1.py (first challenge)
>    - 2.py (second challenge)
>    - \_\_init\_\_.py
>  - \_\_init\_\_.py

<br/>

<table>
  <thead>
    <tr>
      <th style="width:5%;">Day</th>
      <th style="width:5%;">Finished</th>
      <th style="width:15%;">Style</th>
      <th style="width:30%;">Notable Approach</th>
      <th style="width:25%;">Notable Features</th>
      <th style="width:20%;">Other</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.1 <br/> 1.2</td>
      <td>:star: :star:</td>
      <td>Imperative</td>
      <td>/</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td>2.1</td>
      <td>:star:</td>
      <td>Functional</td>
      <td>
        1. Compare every next two level in a tuple.<br>
        - E.g. [7 6 4 2 1] -> (7, 6) -> (6, 4) -> ...<br>
        2. Return False if a rule is broken.<br>
      </td>
      <td>
        1. Immutable and deterministic functions.<br>
        - No side effects.<br>
        - No observable effects outside its scope.<br>
        2. Pipeline design pattern.<br>
        3. Utilizing 'compose' from 'toolz'.<br>
      </td>
      <td>/</td>
    </tr>
    <tr>
      <td>3.1</td>
      <td>:star:</td>
      <td>One-liner</td>
      <td>
        1. Regex to capture pairs of numbers.<br>
        2. Compute the sum of the resulting products.<br>
      </td>
      <td>
        1. Regex with capturing groups.<br>
      </td>
      <td>/</td>
    </tr>
    <tr>
      <td>8.1</td>
      <td>:star:</td>
      <td>Functional</td>
      <td>
        1. Create a list of antennas and coordinates.<br>
        2. Create a list of all possible antinodes.<br>
        3. Remove antinodes not in boundary.<br>
      </td>
      <td>
        1. Using numpy for vector calculations.<br>
      </td>
      <td>
        Note: when you pop an element out of an array, lower the "loop variable".<br>
      </td>
    </tr>
  </tbody>
</table>

</details>
