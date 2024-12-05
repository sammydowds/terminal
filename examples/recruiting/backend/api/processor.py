from terminal.processor import Processor

class ResumeProcessor(Processor):
    def stream_completion(self, content, query):
        """
        Streams the response from OpenAI for a given question and resume content.
        """
        if not content:
            yield "I am sorry, I could not find an exact answer for that."
            return

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
        
        stream = self.openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            temperature=0.5,
            stream=True
        )
        for chunk in stream:
            yield chunk.choices[0].text