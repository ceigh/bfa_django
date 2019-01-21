"""Copyright 2018 Artjom Löbsack

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

from django import template

register = template.Library()


@register.simple_tag
def fingerprint_input():
    return """<script async src='https://cdnjs.cloudflare.com/ajax/libs/js-sha\
3/0.8.0/sha3.min.js'></script>
<script src='https://cdn.jsdelivr.net/npm/fingerprintjs2@2.0.3/dist/fingerprin\
t2.min.js'></script>
<input type='hidden' name='fp'>
<script>Fingerprint2.get(function(e){document.getElementsByName('fp')[0].value\
=sha3_256(e.map(function(e){return e.value}).join())})</script>
"""
