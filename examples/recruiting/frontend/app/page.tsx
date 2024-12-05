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
      <div className="h-max max-md:w-full md:w-[500px] flex flex-col gap-4 pt-4 pb-[90px] max-md:px-4">
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
      <div className="w-full fixed bottom-0 max-w-[500px] max-md:px-4 max-md:bg-white max-md:py-2 max-md:border-t-[1px]">
        <form onSubmit={handleSubmit} className="relative">
          <input
            className="w-full p-2 md:mb-12 border border-gray-300 rounded md:shadow-xl text-[18px]"
            value={input}
            placeholder="Ask something..."
            onChange={handleInputChange}
          />
          <button
            onClick={handleSubmit}
            disabled={isLoading || !input}
            className={cn(
              "absolute top-1 md:right-2 max-md:right-2 p-2 h-9 w-9 border-2 flex items-center justify-center rounded-full bg-blue-600 text-white",
              isLoading || !input ? "bg-stone-300" : "",
            )}
          >
            {isLoading ? (
              <LoaderCircle className="animate-spin" size={16} />
            ) : (
              <Send size={12} />
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
