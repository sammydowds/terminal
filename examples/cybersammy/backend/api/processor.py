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
            Resume Excerpts: {content[:3]}

            Provide a concise, natural response that:
            1. Directly addresses the question
            2. Uses relevant details from the resume excerpt
            3. Maintains a professional tone
            4. Avoids adding information not present in the excerpt
            5. Return an answer in your own words and in less than 4 sentences 
        """
        
        stream = self.openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{ "role": "user", "content": prompt }],
            max_tokens=150,
            temperature=0.1,
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
            else:
                yield ""