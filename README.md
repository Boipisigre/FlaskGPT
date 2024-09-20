# FlaskGPT

C'est un clone simplifier de ChatGPT, dont on trouve
- le code sur [github](https://github.com/DocstringFr/FlaskGPT)
- la video sur [Youtube](https://www.youtube.com/watch?v=AYmcV3b7lWQ)

Quelles différences avec le projet de **DocstringFr**

## Gestion de paquet Python
Je n'ai pass souhaité utiliser *poetry* car j'utilise régulièrement **pipenv**


pour installer les composants nécessaires utiliser  

soit la commande : 
> pipenv -r requirements.txt

si vous ne clonez pas le dépot.

soit la commande : 
> pipenv sync

## CSS et JS
L'installation logiciel se limitera à l'installation de [tailwindCSS](https://tailwindcss.com/blog/standalone-cli)

J'ai récupéré localement les scripts JS et CSS Voir répertoire **dist**

## OpenAI

Il est obligatoire d'avoir un compte [OpenAI](https://openai.com/) payant pour utiliser les API

Parailleurs la version de la lbrairie *OpenAi* Python proposée est ancienne, J'ai installé la version 1.41.0
ce qui a occasionné
- un changement dans l'import openai
- un changement dans le chargement de la clef

> openai.api_key = os.getenv("OPENAI_API_KEY")

remplacé par
> client = OpenAI( api_key = os.getenv("API_KEY"), )

- un changement dans l'appel de la fonction
~ChatCompletion.create~
que l'on doit remlacer par  **chat.completions.create**
