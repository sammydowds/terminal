import { useQuery, UseQueryOptions } from "@tanstack/react-query";

const RELATED_API = process.env.NEXT_PUBLIC_RELATED_API ?? "";

const searchProducts = async (query: string) => {
  const res = await fetch(RELATED_API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });
  const data = await res.json();
  return data.data;
};

export const useSearchProducts = (
  query: string,
  options?: Partial<UseQueryOptions>,
) => {
  return useQuery({
    queryKey: ["products", query],
    queryFn: () => searchProducts(query),
    ...options,
  });
};
