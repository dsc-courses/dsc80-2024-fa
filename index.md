---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

[syllabus]: syllabus
[ed]: https://edstem.org/us/join/zk8hRm
[gradescope]: https://www.gradescope.com/courses/698219
[github]: https://github.com/dsc-courses/dsc80-2024-sp
[welcome-survey]: https://forms.gle/zSYRnDK7wNUWehPh8
[exam-accommodations]: https://forms.gle/rSUYPsHdmxTN9qYv5
[extension-request-form]: https://forms.gle/yK1tcVZRpxHPBN1w9

<!-- [Jump to the current week](#week-9-modeling-in-practice){: .btn } [Lab Solutions](https://edstem.org/us/courses/51951/discussion/4183397){: .btn .btn-green } -->

[Podcasts](https://podcast.ucsd.edu/){: .btn }
[Welcome Survey][welcome-survey]{: .btn }
[Exam Accommodations Form][exam-accommodations]{: .btn }
[Extension Request Form][extension-request-form]{: .btn }

<!-- Click the 🎥 button to view the recording of a lecture/discussion.<br>Click the 📝 button to view lecture notebooks after they've been filled in during lecture. -->

<!-- {: .green }
**Welcome to DSC 80! 👋 Make sure to: read the [syllabus][syllabus], check that you can access [Gradescope][gradescope] and [Ed][ed], fill out the [Welcome Survey][welcome-survey], and fill out the [Exam Accommodations Form][exam-accommodations] if you have an exam conflict.** -->

{% for module in site.modules %}
{{ module }}
{% endfor %}
