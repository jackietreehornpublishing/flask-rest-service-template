# Python microservice template using Flask

This template is the baseline for a [Flask](http://flask.pocoo.org/) based project.

## Flask structure

This template generates a Flask based microservice following, as best as it can, the general
packaging rules for small Flask projects. It does not rely on [blueprints](http://flask.pocoo.org/docs/0.10/blueprints/)
as they seem a little overkill for a microservice. If the community prefers them, we will be able to
upgrade this microservice.

In effect, a microservice should be its own blueprint. But we can revisit.

## Default modules vs contract based modules

The code is made of fairly static templates that may be overwritten if a contract service was provided.
For instance `swagger.py` and `swagger_tpl.py`. The former one exist to provide a default swagger endpoint
advertising the default / endpoint. This only exists when no contract was passed to the template.
Otherwise, `swagger_tpl.py` and `views_tpl.py` overwrite the default ones.

## Python version in the Dockerfile

In order to be as modern as possible, the Dockerfile relies on Python 3.5. This is where the Python
ecosystem is heading. However, this may not work well with some dependencies that still expect Python
2.x. In that case, the user will have to amend the Dockerfile. Or, we could specify the target Python
version as a new parameter.

