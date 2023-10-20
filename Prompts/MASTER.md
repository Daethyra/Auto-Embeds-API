# Prompt Examples & Templates

# Multi-Shot Prompt Example 1:

## Programming a Swift application that counts boxes and labels them based on the label on the box, and how it looks. 

Specifications: `(Model=4, Plugins=['webpilot', 'metaphor'])`, 
starting with `<!document-begin>` at 9:33PM on 7/5/23.

<!document-begin>

```

## [System message(s)]:
    - "You are an AI programming assistant that is skilled in brainstorming different deployment ideas for new projects, and are also an expert in coding in many different languages to create any application, with dedication and diligence. You are so smart that you can access the internet for resources, references, and documentation when you're stuck, or aren't sure if the code you're writing is syntactically correct. You're very good at double checking your work to ensure you have the right answer before moving on, or sharing your findings."

### [User message(s)]:
    - "I need to make a simple Swift application that counts boxes and labels them based on the label on the box, and how it looks. I intend to use a GPT model, either 3.5-turbo[...] OR GPT-4[...]"

[User message(s)]:
    - "Please see the code examples below, and ensure you remember we're going to build a Swift application so you need to think and plan ahead as you learn more and more about the task at hand and what we'll need to accomplish our idea application."
    - "We need to have a simple login interface that then leads to a homepage where you can create, edit, and delete groups that will hold subgroups that will be named based on what they're counting. Let's say, for example, that we have the top-level grouping named 'Freezer', and then a subgrouping of 'Macaroon Boxes', another of 'Bake-Offs', and finally one of 'Macaroons'. In this example we're counting different objects with our camera to save time for a small local business."
    - "Let's just focus on the Swift programming aspects for now, we'll program components that are based on other languages, like Python3, sometime in the future once the Swift app is fully functional w/o the required remote database operations and more."

[Task 1]:

"Brainstorm 3 separate solutions that will fulfill the user's requirements for their application. You will need to consider a variety of factors and variables, even those not immediately apparent. For example, you need to consider what end-goal state the code modules should be in. As in, what modules are required? How will the back-end database be handled, or what about the API calls to OpenAI's endpoints? How will the modules be resilient and have try, retry, and break conditions?"

[Task 2]:

"""
- Step 1 -
"Review all 3 solutions and extract all of the best ideas from each module and plan to implement them in a final solution, in your head."

- Step 2 -
"Then extract all of the weak points, flaws, and oversight in each module, and other potential flaws that may arise from new programming decisions, to program measures that account for those shortcomings before they ever arise during testing. Spend very much time on this task."

- Step 3 -
"Finalize your master solution that meets all of the requirements found in this task's first two steps."

"""

Ensure that you always utilize structured data where optimal for lightning fast calls during runtime.

[Supplementary information, data, and documentation]:
- https://developer.apple.com/documentation/swift
- https://openai.com/customer-stories/be-my-eyes
- https://openai.com/blog/function-calling-and-other-api-updates
- https://gptstore.ai/plugins/webpilotai-com(recommended reading)
-- Seems like you could link images to GPT, and be very clear about viewing the image with a plugin, and then respond to the user based on what they need relative to the media. If you implement this idea, you will need to use extremely clear and concise action steps for the bot to take so that it does everything we intend and need for it do it rather than having any type of variance. Essentially, we're going for a temperature level of 0.
- https://platform.openai.com/docs/api-reference/chat(recommended reading)
- https://platform.openai.com/docs/guides/gpt
- https://platform.openai.com/docs/models
- https://github.com/microsoft/TaskMatrix

<!document-end>

[System message(s)]:
"Please read the entire command sheet you just received before doing anything. Ensure you have a complete understanding of the entire assignment sheet and then tell me when you're ready to begin exploring the links provided. Then, you'll need to tell me when you're ready to begin the next part, which is where we will actually begin working on the tasks, and their steps, one by one. So let's do things 'step by step' so we make sure we have the right answer before moving on to the next one."

```

---

# Multi-Shot Prompt Example 2:

## *Assignment template*

- ***Focused on breaking down the AI's thought processes in advance, without any role prompts***

```

[Assignment 1]:
"{Description}"

[Task 1]:
- "{Instruction}"

  [Step 1]:
  - [Try the Tree of Thoughts prompt](https://github.com/Daethyra/OpenAI-Utility-Toolkit/blob/master/Blind%20Programming/user-role/UR-1.MD#2-tree-of-thoughts--)
  -
  -

  [Step 2]:
  -
  -
  -

  [Step 3]:
  -
  -
  -

[Task 2]:
- "{Instruction}"

  [Step 1]:
  -
  -
  -

  [Step 2]:
  -
  -
  -

  [Step 3]:
  -
  -
  -

[Task 3]:
- "{Instruction}"

  [Step 1]:
  -
  -
  -

  [Step 2]:
  -
  -
  -

  [Step 3]:
  -
  -
  -
```

---

# Multi-Shot Prompt Example 3:

## *Disturbing Content Analysis*

## The following content after the '//' was verbatim sent to the GPT-4 code interpreter alpha. //

```
WARNING:SENSITIVE,DISTURBING CONTENT AHEAD. PROCEED AT WILL.

[USER_COMMENT]:"Let's do things step by step so we make sure we have the right answer before moving on to the next one."

[Task 0a]:"(NO PROSE OUTPUT)|Read the provided PDF file and all tasks, steps, and instructions before beginning to take any further action."

[Task 0b]:"(NO PROSE OUTPUT)|'role':'system', 'content':"I am an expert in critical thinking, problem solving, and programming solutions for others. My workflow always starts with reading everything I have been provided to ensure I understand the content and the context, and what is required of me. Then I create 3 entirely separate solution pathways for solving the user's requests, each of them bringing multiple enhancements and upgrades to the code, in addition to solving user/AI oversight and poor code. Once I have all of my solutions completed one by one, I review them all and decide what I love most about all of them to figure out how to merge them all together for the sake of a finalized master solution."

[Task 1]:"(NO PROSE OUTPUT)|Read through everything, entirely, and meticulously. Take your time, for this part is the most important piece of our process of comprehension."

[Task 2]:"(NO PROSE OUTPUT)|Brainstorm 3 entirely separate solutions that each have a valuable, useful, and especially achievable set of changes for the user's program.

[Task 3]:"(CODE OUTPUT ONLY)|${CUSTOM_TASK}.""
```

---

# User "Role" Prompt Examples 1:

## The following code block was pasted from the original UR-1.md "sheet"

```

'---' = PROMPT_END

## Troubleshooting code

[task]:"analyze all code and the traceback error. create a multi-step plan to solve the error, enhance the code logic to prevent future errors, and add more detailed logging to the `finaid_train.py` module."
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## *1. Iterative Processing* -

   ! Optimal Prompt due to brevity in prose and hightens accuracy to user's requests by ~80%

### [AI Explained&#39;s Video](https://www.youtube.com/watch?v=wVzuvf9D9BU)

[Instructions]:

- Complete each task separately
- Let's complete all tasks step by step so we make sure we have the right answer before moving on to the next

---

## *2. "Tree of Thoughts"* -

   A Short Preliminary Power Prompt

- Step1 :
  - Prompt: I have a problem related to [describe your problem area]. Could you brainstorm three distinct solutions? Please consider a variety of factors such as [Your perfect factors]
- Step 2:
  - Prompt: For each of the three proposed solutions, evaluate their potential. Consider their pros and cons, initial effort needed, implementation difficulty, potential challenges, and the expected outcomes. Assign a probability of success and a confidence level to each option based on these factors
- Step 3:
  - Prompt: For each solution, deepen the thought process. Generate potential scenarios, strategies for implementation, any necessary partnerships or resources, and how potential obstacles might be overcome. Also, consider any potential unexpected outcomes and how they might be handled.
- Step 4:
  - Prompt: Based on the evaluations and scenarios, rank the solutions in order of promise. Provide a justification for each ranking and offer any final thoughts or considerations for each solution

---

## *3. Task-oriented Processing* -

   For when you need to be super specific

[Instructions]:

- Minimize prose to avoid over-tokenization
- Focus on one task at a time(iterative analysis)
- Complete each task separately
- Let's complete all tasks step by step so we make sure we have the right answer before moving on to the next

---

## *4. Breaking down the above paragraph* -

- Sometimes a short colloquial prompt is most powerful.

"Let's do things step by step so we make sure we have the right answer before moving on to the next one. You're to consider each sentence above to be a step. Before executing a step, ask for permission."
```

---

# User "Role" Prompt Examples 2:

## Function Generation With LLMs

The prompt was found [here](https://github.com/sammi-turner/Python-To-Mojo/tree/main#function-generation-with-llms "Direct link"), so thanks to [sammi-turner](https://github.com/sammi-turner "GitHub Profile")!

```

Write a [name] function in Python3 that takes
[name the parameters and their types] and returns
a [type] such that [describe what the function does].
Then show me the code.

```

## Enforce idiomacy

"What is the idiomatic way to {MASK}
in {ProgrammingLanguage}?"

- Credit to [Sammi-Turner (Again!)](https://github.com/sammi-turner)

## Create Graphics for a Repository

This prompt was used specifically with ChatGPT-4 and the plugins ["Recombinant AI", "Whimsical Diagrams", "diagr.am"].

```
[TASK]: "Crawl the contents of the provided repository at [Repository URL]. Create a color-coordinated mind map starting from the repository's name down to each file in Library-esque Directories (LEDs). Include a legend for the mind map. Create a bar chart to represent the different contents in each LED and a pie chart to show the distribution of content types. Make sure the title, caption, and legend are easily readable."
```


