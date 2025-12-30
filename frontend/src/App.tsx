import ChatWindow from "./components/ChatWindow";

export default function App() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center">
      <div className="w-full max-w-5xl h-[85vh] bg-[#0f172a] border border-[#1f2937] rounded-2xl shadow-2xl flex flex-col">
        {/* Header */}
        <div className="px-6 py-4 border-b border-[#1f2937] flex items-center gap-3">
          <div className="w-3 h-3 rounded-full bg-gradient-to-br from-violet-500 to-cyan-400" />
          <h1 className="text-lg font-semibold">Memory-Augmented AI</h1>
        </div>

        {/* Chat */}
        <ChatWindow />
      </div>
    </div>
  );
}
