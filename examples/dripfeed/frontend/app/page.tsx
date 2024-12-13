"use client";

import { Input } from "@/components/ui/input";
import { useSearchProducts } from "@/hooks/useSearchProducts";
import { Globe } from "lucide-react";
import { useEffect, useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [debouncedQuery, setDebouncedQuery] = useState("");
  const { data: products } = useSearchProducts(debouncedQuery, {
    enabled: !!debouncedQuery?.length,
    retry: false,
  });

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedQuery(query);
    }, 1000);
    return () => {
      clearTimeout(handler);
    };
  }, [query]);

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setQuery(val);
  };

  return (
    <div className="m-24 flex flex-col gap-4 justify-center items-center">
      <div className="max-w-[800px] flex flex-col gap-4">
        <div>
          <h1 className="text-[24px] font-bold tracking-tighter leading-4 flex items-center gap-[3px]">
            <Globe color="lightgray" strokeWidth={1} />
            Dripfeed
          </h1>
          <h2 className="text-[16px] tracking-tighter text-stone-400">
            Tell us what you are looking for.
          </h2>
        </div>
        <div className="flex flex-col items-center gap-2">
          <Input
            className="md:text-[16px] max-md:text-[16px] rounded-sm md:min-w-[500px] max-md:min-w-[300px]"
            value={query}
            onChange={onChange}
            placeholder="A jacket for winter..."
          />
        </div>
        <div className="flex flex-col">
          {products?.map((p) => {
            return (
              <div key={p.id} className="flex gap-2 my-2">
                <img
                  className="rounded-lg"
                  src={p.image}
                  alt={p.name}
                  height={100}
                  width={100}
                />
                <div className="max-w-[300px]">
                  <div className="text-md font-semibold">{p.name}</div>
                  <div className="text-xs">{p.long_description}</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
