- we already worked/return with static html data
- now, we will worked/return with dynamic/custom html data.


## what is template engine?
- used for dynamic html data

- #### context:
    - from backend to html, we pass the data via context
        - return render(request, "index.html", context={'peoples' : peoples})
        
    - then inside the html: just {{peoples}}
    - to use for loop of python or other utilities:
        - {% for people in peoples %} 
            --- html codes ---
        {% endfor %}


- [django template tags](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
- for variable: {{ ... }}
- for utility/scope: {% start %} ... {% end %}
- to show just specific characters of a text: {{text|truncatechars:80}}
    - just show 80 first 80 characters


- ### DRY: Don't Repeat Yourself
    - all common patr or code we will store into base.html
    - just codes vary inside the block
    - but all title will same, so we will pass context from views.py to custom title
        - we will use same variable name for each page


- Refactor Python instantly with Sourcery --> add extention