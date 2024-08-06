# Contributing to Open Medical Reasoning Tasks

Thank you for your interest in contributing to the **Open Medical Reasoning Tasks** project! Your expertise is crucial in building a comprehensive collection of LLM reasoning tasks in the healthcare domain.

To contribute, please use GitHub and follow these guidelines. If you're not familiar with GitHub, don't worry! You can use [this Google form](https://forms.gle/Gz1qp4Vdm2aXUZjDA
) to submit your tasks. 
Make sure to check [the example provided](https://github.com/openlifescience-ai/Open-Medical-Reasoning-Tasks/blob/main/tasks/clinical-diagnosis-formulation.md) to ensure all information is filled out correctly. 

## How to Contribute

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/YourUsername/Open-Medical-Reasoning-Tasks.git
   ```

3. **Create a New Branch**: Create a new branch for your contribution.
   ```bash
   git checkout -b add-new-medical-task
   ```

4. **Add Your Task**: To add a new task, you need to do two things:
   a. Add a new row to the `tasks.md` file in the root directory.
   b. Create a new file in the `tasks/` directory for your task.

5. **Update tasks.md**: Add a new row to the table in `tasks.md` using this format:
   ```markdown
   | Task Name | Brief description of the medical reasoning task. |
   ```
   Ensure the task name is in title case and the link uses lowercase with hyphens.

6. **Create Task File**: In the `tasks/` directory, create a new file named `task-name.md` (use lowercase and hyphens). Use the template provided in [tasks/task-template.md](task-template.md).

7. **Build the Task**: Tasks are stored in JSON, but are contributed in markdown. Run `run.py` to convert the markdown to JSON, and then convert it back. This will ensure that the markdown is correctly formatted, and that the structured data contained within the task has been logged correctly. If something about the markdown in your reconstructed file is off, you likely submitted the task incorrectly.

8. **Commit Your Changes**: Commit your changes with a meaningful commit message.
   ```bash
   git add tasks.md tasks/your-new-medical-task.md
   git commit -m "Add new medical task: Task Name"
   ```

9. **Push Your Branch**: Push your branch to your forked repository.
   ```bash
   git push origin add-new-medical-task
   ```

10. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request from your forked repository. Provide a clear description of the medical reasoning task you are submitting and its relevance to healthcare AI.

## Guidelines

- Ensure your task is clear, well-defined, and relevant to medical reasoning.
- Provide multiple healthcare-specific examples to illustrate the task.
- Use relevant medical and AI tags to categorize your task.
- Follow the existing format and style of the repository.
- Make sure your task file name matches the link in tasks.md.
- Consider the ethical implications and potential biases in medical AI when designing tasks.

## Task Content

Your task should include:
- A clear description of the medical reasoning challenge
- At least two examples with input and expected output
- Relevant tags (e.g., diagnosis, treatment planning, medical image interpretation)
- Any necessary context or background information for the task

Remember, your contributions will help build better medical seed tasks and synthetic training datasets for open medical AI, ultimately leading to improved, bias-free language models in healthcare.

Thank you for contributing to the advancement of AI in healthcare!
