"use client";

import { useChat } from "ai/react";
import { twMerge as cn } from "tailwind-merge";
import { useEffect, useRef } from "react";
import { LoaderCircle, Send } from "lucide-react";

export default function Home() {
  const { input, handleInputChange, handleSubmit, messages, isLoading } =
    useChat({
      api: process.env.NEXT_PUBLIC_CHAT_API,
      streamProtocol: "text",
    });

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex flex-col items-center justify-center min-h-dvh overflow-y-auto bg-stone-100 text-black relative">
      <div className="h-max max-md:w-full md:w-[500px] flex flex-col gap-4 pt-4 md:pb-[200px] max-md:pb-[140px] max-md:px-4">
        {messages.map((m) => (
          <div key={m.id} className="w-full flex flex-col">
            <div
              className={cn(
                "max-w-[80%] p-2 shadow rounded-lg text-[14px] bg-white",
                m.role === "user"
                  ? "self-end bg-blue-600 text-white"
                  : "self-start",
              )}
            >
              {m.content}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="w-full fixed bottom-0 max-w-[500px] max-md:bg-white max-md:py-2 max-md:border-t-[1px]">
        <div className="flex flex-wrap max-md:flex-nowrap max-md:overflow-x-auto gap-2 my-2 max-md:px-2 w-full">
          {[
            "Have you used React?",
            "Where did you go to college?",
            "What year did you graduate college?",
          ].map((question) => (
            <button
              key={question}
              className="px-4 py-[4px] bg-white border-[1px] whitespace-nowrap border-stone-500 border-dashed text-stone-600 text-sm rounded-full"
              onClick={() => handleInputChange({ target: { value: question } })}
            >
              {question}
            </button>
          ))}
        </div>
        <form onSubmit={handleSubmit} className="relative max-md:px-2">
          <input
            className="w-full p-3 md:mb-12 border border-gray-300 rounded text-[18px]"
            value={input}
            placeholder="Ask something..."
            onChange={handleInputChange}
          />
          <button
            onClick={handleSubmit}
            disabled={isLoading || !input}
            className={cn(
              "absolute top-1 md:right-2 max-md:right-3 p-2 h-11 w-11 border-2 flex items-center justify-center rounded-full bg-blue-600 text-white",
              isLoading || !input ? "bg-stone-300" : "",
            )}
          >
            {isLoading ? (
              <LoaderCircle className="animate-spin" size={16} />
            ) : (
              <Send size={20} />
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
