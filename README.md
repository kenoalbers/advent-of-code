# [Advent of Code :christmas_tree:](https://adventofcode.com)
Exploring new languages, features, and packages while learning and experimenting with different programming paradigms,
patterns, and approaches.

View the description for highlights of the day, unique features, programming styles, notable approaches, 
and distinctive characteristics demonstrated in the solution.

> **Note:**  
> No files share any contents except through the shared folder.
> Challenge part 1 and 2 are independent of one another and code is copied for part 2.

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
      <th style="width:5%">Day</th>
      <th style="width:5%">Finished</th>
      <th style="width:15%">Style</th>
      <th style="width:30%">Notable Approach</th>
      <th style="width:25%">Notable Features</th>
      <th style="width:20%">Other</th>
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
        <ul>
          <li>Compare every next two level in a tuple.</li>
          <ul>
            <li>[7 6 4 2 1] -> (7, 6) -> (6, 4) -> ...</li>
          </ul>
          <li>Return False if a rule is broken.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Immutable and deterministic functions</li>
          <ul>
            <li>No side effects</li>
            <li>No observable effects outside its scope</li>
          </ul>
          <li>Pipeline design pattern</li>
          <li>Utilizing 'compose' from 'toolz'</li>
        </ul>
      </td>
      <td>/</td>
    </tr>
    <tr>
      <td>3.1</td>
      <td>:star:</td>
      <td>One-liner</td>
      <td>
        <ul>
          <li>Regex to capture pairs of numbers.</li>
          <li>Compute the sum of the resulting products.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Regex with capturing groups.</li>
        </ul>
      </td>
      <td>/</td>
    </tr>
    <tr>
      <td>8.1</td>
      <td>:star:</td>
      <td>Functional</td>
      <td>
        <ul>
          <li>Create a list of antennas and coordinates.</li>
          <li>Create a list of all possible antinodes.</li>
          <li>Remove antinodes not in boundary.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Using numpy for vector calculations.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Note: when you pop an element out of an array, lower the "loop variable"</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

</details>
