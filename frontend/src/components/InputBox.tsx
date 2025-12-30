export default function InputBox({
    onSend,
    disabled,
  }: {
    onSend: (msg: string) => void;
    disabled: boolean;
  }) {
    let text = "";
  
    return (
      <div className="p-4 border-t border-[var(--border)] bg-[#0b0f14]">
        <div className="flex gap-2 bg-[#020617] border border-[var(--border)] rounded-xl p-2">
          <input
            className="flex-1 bg-transparent outline-none text-sm px-2"
            placeholder="Ask something intelligent…"
            disabled={disabled}
            onChange={(e) => (text = e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && onSend(text)}
          />
          <button
            disabled={disabled}
            onClick={() => onSend(text)}
            className="px-4 rounded-lg gradient-accent text-white text-sm hover:opacity-90 transition disabled:opacity-40"
          >
            Send
          </button>
        </div>
      </div>
    );
  }
  