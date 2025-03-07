function generateQuiz(containerId, title, question, options, correctAnswer) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear previous content

    const questionTitle = document.createElement('p');
    questionTitle.textContent = title;
    questionTitle.style.fontWeight = 'bold';
    questionTitle.style.color = '#F78F2E';
    questionTitle.style.marginBottom = '0px';
    container.appendChild(questionTitle);

    const questionElement = document.createElement('p');
    questionElement.textContent = question;
    questionElement.style.marginBottom = '5px';
    container.appendChild(questionElement);

    const form = document.createElement('form');
    form.id = `form-${containerId}`; // Unique form ID to avoid conflicts

    const messageElement = document.createElement('div');
    messageElement.style.opacity = 0;
    messageElement.style.transition = 'opacity 0.2s ease-in-out';
    messageElement.style.display = 'none';
    messageElement.style.color = 'black';
    messageElement.style.padding = '10px';
    messageElement.style.borderRadius = '5px';
    messageElement.style.marginTop = '10px';
    messageElement.style.fontSize = '15px';

    const messageBody = document.createElement('div');
    messageElement.appendChild(messageBody);

    Object.entries(options).forEach(([option, explanation], index) => {
        const div = document.createElement('div');
        div.className = 'form-check d-flex align-items-center'; // Flexbox for vertical alignment

        const input = document.createElement('input');
        input.type = 'radio';
        input.name = `quiz-${containerId}`; // Unique name for each quiz instance
        input.value = option;
        input.className = 'form-check-input me-2'; // Added margin for spacing
        input.id = `option-${containerId}-${index}`;
        input.style.marginTop = '0'; // Ensure no extra space pushes text down
        input.style.borderColor = '#4853A4'; // Radio button outline
        input.style.boxShadow = 'none';  // Remove brief occurances of transparent fill when clicked
        input.style.outline = 'none';  // Remove brief occurances of transparent fill when clicked


        input.addEventListener('change', function () {
            messageElement.style.display = 'none';
            messageElement.style.opacity = 0;

            if (option === correctAnswer) {
                const emojis = ["🍀", "🎉", "🌈", "🚀", "🌟", "✨", "💯"]
                const emoji = emojis[~~(Math.random() * emojis.length)]
                messageBody.innerHTML = `<strong style="color: #F78F2E; !important; font-size: 16px">Correct! &nbsp;${emoji}</strong><br>${explanation}`;
                messageElement.style.backgroundColor = '#FEEFE1'; // Light background for content
                messageElement.style.borderLeft = '5px solid #F78F2E'; // Left border styling
            } else {
                messageBody.innerHTML = `<strong style="color: #4853A4 !important; font-size: 16px;">Incorrect</strong><br>${explanation}`;
                messageElement.style.backgroundColor = '#E1E3F0'; // Light background for content
                messageElement.style.borderLeft = '5px solid #4853A4'; // Left border styling
            }

            messageElement.style.display = 'block';
            setTimeout(() => messageElement.style.opacity = 1, 10);
        });

        const label = document.createElement('label');
        label.className = 'form-check-label';
        label.setAttribute('for', `option-${containerId}-${index}`);
        label.textContent = option;
        label.style.marginBottom = '3px'; // Ensure text remains aligned

        div.appendChild(input);
        div.appendChild(label);
        form.appendChild(div);
    });

    container.appendChild(form);
    container.appendChild(messageElement);

    const spacing = document.createElement('div');
    spacing.style.marginBottom = '30px';
    container.appendChild(spacing);
}
