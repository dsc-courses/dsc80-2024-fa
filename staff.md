---
layout: page
title: 👩‍🏫 Staff
description: A listing of all the course staff members.
nav_order: 6
---

# 👩‍🏫 Staff

## Instructor

<div class="staffer">
  <img class="staffer-image" src="/assets/staff-images/lau.jpg" alt="Sam Lau">

  <div>
    <h3 class="staffer-name">
      <a href="https://www.samlau.me/">Sam Lau</a>
    </h3>

    <!-- Contact Information -->
    <p>
      <a href="mailto:lau@ucsd.edu">lau@ucsd.edu</a><br>
    </p>

    <!-- Instructor Paragraph -->
    <p>
    Sam Lau is an assistant teaching professor in the Halıcıoğlu Data Science Institute at UC San Diego. His research creates novel interfaces for learning and teaching data science, including the popular Pandas Tutor tool (<a href="https://pandastutor.com/" target="_blank">https://pandastutor.com/</a>) which serves over 40,000 people per year. He is the author of an introductory data science textbook called Learning Data Science, published by O’Reilly Media in 2023.
    </p>
  </div>
</div>


## Staff

{% assign tas = site.staffers | where: 'role', 'TA' %}
{% for staffer in tas %}
{{ staffer }}
{% endfor %}

{% assign staff = site.staffers | where: 'role', 'Tutor' %}
<div class="role">
  {% for staffer in staff %}
  {{ staffer }}
  {% endfor %}
</div>
