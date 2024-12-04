from terminal.processor import Processor

class ResumeProcessor(Processor):
    def process_content(self, content, query):
        """
        Given the relevant content, create a response to the users questions.
        """
        if not content:
            return "I am sorry, I could not find an exact answer for that."
        prompt = f"""Given a question about a resume and a relevant excerpt from that resume, provide a clear, 
            professional response that connects the resume content to the question asked. Focus on highlighting relevant 
            skills, experiences, and achievements.

            Question: {query}
            Resume Excerpt: {content[0]}

            Provide a concise, natural response that:
            1. Directly addresses the question
            2. Uses relevant details from the resume excerpt
            3. Maintains a professional tone
            4. Avoids adding information not present in the excerpt
        """
        response = self.openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()