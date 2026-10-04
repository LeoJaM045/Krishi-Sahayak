import React, { useState, useEffect, useRef } from 'react';
import { Send, Globe2, Loader2, Info, ChevronDown, ChevronUp, Copy, Check } from 'lucide-react';
import { api } from '../utils/api';

const QuickReplies = ({ onSelect }) => {
  const replies = [
    { text: 'ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?', icon: '🌾' },
    { text: 'ਝੋਨੇ ਨੂੰ ਪਾਣੀ ਕਦੋਂ ਲਾਈਏ?', icon: '💧' },
    { text: 'ਮੇਰੀ ਫਸਲ ਨੂੰ ਕੀੜਾ ਲੱਗ ਗਿਆ', icon: '🐛' },
    { text: 'ਅੱਜ ਦਾ ਮੌਸਮ ਕਿਵੇਂ ਹੈ?', icon: '🌦️' },
  ];
  return (
    <div className="flex flex-wrap gap-2 mb-4">
      {replies.map((reply, i) => (
        <button
          key={i}
          onClick={() => onSelect(reply.text)}
          className="bg-white border border-gray-200 hover:border-agri-400 hover:text-agri-600 px-4 py-2 rounded-full text-sm font-medium transition-all shadow-sm flex items-center gap-2"
        >
          <span>{reply.icon}</span>
          {reply.text}
        </button>
      ))}
    </div>
  );
};

const NLPAnalysis = ({ nlp }) => {
  const [open, setOpen] = useState(false);
  if (!nlp) return null;

  return (
    <div className="mt-2 text-xs bg-gray-50 border border-gray-100 rounded-lg overflow-hidden">
      <button 
        onClick={() => setOpen(!open)} 
        className="w-full flex items-center justify-between p-2 text-gray-500 hover:bg-gray-100"
      >
        <span className="flex items-center gap-1 font-medium"><Info className="w-3 h-3" /> NLP Analysis</span>
        {open ? <ChevronUp className="w-3 h-3" /> : <ChevronDown className="w-3 h-3" />}
      </button>
      {open && (
        <div className="p-3 border-t border-gray-100 grid grid-cols-2 gap-2 text-gray-600 font-mono">
          <div><span className="font-semibold">Language:</span> {nlp.language}</div>
          <div><span className="font-semibold">Intent:</span> {nlp.intent}</div>
          <div><span className="font-semibold">Confidence:</span> {(nlp.confidence * 100).toFixed(1)}%</div>
          <div className="col-span-2">
            <span className="font-semibold">Entities:</span> 
            {Object.keys(nlp.entities).length > 0 ? (
              <pre className="mt-1 bg-white p-1 rounded border border-gray-100 text-[10px]">
                {JSON.stringify(nlp.entities, null, 2)}
              </pre>
            ) : " None"}
          </div>
        </div>
      )}
    </div>
  );
};

const Message = ({ msg, translateAll }) => {
  const isBot = msg.sender === 'bot';
  const [translated, setTranslated] = useState(null);
  const [autoTranslated, setAutoTranslated] = useState(null);
  const [translating, setTranslating] = useState(false);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    let isMounted = true;
    if (translateAll) {
      setTranslating(true);
      api.translate(msg.text, 'punjabi', 'english').then(res => {
        if (isMounted) {
          setAutoTranslated(res.translated_text || res.translatedText || msg.text);
          setTranslating(false);
        }
      }).catch(e => {
        console.error(e);
        if (isMounted) {
          setAutoTranslated(null);
          setTranslating(false);
        }
      });
    } else {
      setAutoTranslated(null);
      setTranslated(null);
    }
    return () => { isMounted = false; };
  }, [translateAll, msg.id]);

  const handleTranslate = async () => {
    if (translated) {
      setTranslated(null);
      return;
    }
    setTranslating(true);
    try {
      const targetLang = (msg.nlp?.language === 'english') ? 'punjabi' : 'english';
      const res = await api.translate(msg.text, 'auto', targetLang);
      setTranslated(res.translated_text);
    } catch (e) {
      console.error(e);
    }
    setTranslating(false);
  };

  const copyText = () => {
    navigator.clipboard.writeText(msg.text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className={`flex flex-col ${isBot ? 'items-start' : 'items-end'} mb-4`}>
      <div className={`max-w-[85%] md:max-w-[70%] p-4 rounded-2xl shadow-sm ${isBot ? 'bg-white border border-gray-100 rounded-tl-none' : 'bg-agri-600 text-white rounded-tr-none'}`}>
        <p className="whitespace-pre-wrap leading-relaxed">{msg.text}</p>
        
        {(autoTranslated || translated) && (
          <div className="mt-3 pt-3 border-t border-gray-200/50 text-sm opacity-90">
            <p className="font-medium text-xs mb-1 opacity-70">Translation:</p>
            {autoTranslated || translated}
          </div>
        )}

        {isBot && (
          <div className="mt-3 flex items-center justify-between text-gray-400">
            <div className="flex gap-2">
              {!autoTranslated && (
                <button onClick={handleTranslate} className="hover:text-agri-600 transition-colors" title="Translate">
                  {translating ? <Loader2 className="w-4 h-4 animate-spin" /> : <Globe2 className="w-4 h-4" />}
                </button>
              )}
              <button onClick={copyText} className="hover:text-agri-600 transition-colors" title="Copy">
                {copied ? <Check className="w-4 h-4 text-green-500" /> : <Copy className="w-4 h-4" />}
              </button>
            </div>
            <span className="text-[10px] uppercase tracking-wider">Krishi Sahayak</span>
          </div>
        )}
      </div>
      {isBot && msg.nlp && <NLPAnalysis nlp={msg.nlp} />}
    </div>
  );
};


export default function Chatbot() {
  const [messages, setMessages] = useState([
    { id: 1, text: "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! 🌾\nਮੈਂ ਪੰਜਾਬੀ ਕ੍ਰਿਸ਼ੀ ਸਹਾਇਕ ਹਾਂ। ਤੁਸੀਂ ਖੇਤੀਬਾੜੀ ਨਾਲ ਸਬੰਧਤ ਕੋਈ ਵੀ ਸਵਾਲ ਪੰਜਾਬੀ ਵਿੱਚ ਪੁੱਛ ਸਕਦੇ ਹੋ।", sender: "bot" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [sessionId] = useState(() => Math.random().toString(36).substring(7));
  const messagesEndRef = useRef(null);
  const [translateAll, setTranslateAll] = useState(false);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSend = async (text = input) => {
    if (!text.trim()) return;
    
    const userMsg = { id: Date.now(), text, sender: 'user' };
    setMessages(prev => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const data = await api.chat(text, sessionId);
      const botMsg = {
        id: Date.now() + 1,
        text: data.response,
        sender: 'bot',
        nlp: {
          intent: data.intent,
          confidence: data.confidence,
          language: data.language,
          entities: data.entities
        }
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      console.error(error);
      setMessages(prev => [...prev, { id: Date.now() + 1, text: "ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਨਹੀਂ ਹੋ ਸਕਿਆ। (Connection Error)", sender: 'bot' }]);
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-2rem)] md:h-[calc(100vh-4rem)] max-w-4xl mx-auto relative">
      <div className="flex justify-between items-center mb-4 relative">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">Chat</h2>
          <p className="text-gray-500 text-sm">Ask your agricultural queries</p>
        </div>
        <div className="relative">
          <button 
            onClick={() => setTranslateAll(!translateAll)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg border shadow-sm transition-colors font-medium text-sm ${translateAll ? 'bg-agri-600 text-white border-agri-600' : 'bg-white border-gray-200 hover:border-agri-300 hover:text-agri-600'}`}
          >
            <Globe2 className="w-4 h-4" /> {translateAll ? 'Show Original' : 'Translate to English'}
          </button>
        </div>
      </div>

      <div className="flex-1 bg-gray-50/50 rounded-2xl border border-gray-200/60 overflow-hidden flex flex-col shadow-sm">
        <div className="flex-1 overflow-y-auto p-4 md:p-6 scroll-smooth">
          {messages.length === 1 && <QuickReplies onSelect={handleSend} />}
          
          {messages.map(msg => (
            <Message key={msg.id} msg={msg} translateAll={translateAll} />
          ))}
          {loading && (
            <div className="flex items-start mb-4">
              <div className="bg-white border border-gray-100 p-4 rounded-2xl rounded-tl-none shadow-sm flex gap-2 items-center text-gray-400">
                <div className="w-2 h-2 bg-agri-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-agri-400 rounded-full animate-bounce" style={{animationDelay: "0.2s"}}></div>
                <div className="w-2 h-2 bg-agri-400 rounded-full animate-bounce" style={{animationDelay: "0.4s"}}></div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-gray-100">
          <form 
            onSubmit={(e) => { e.preventDefault(); handleSend(); }}
            className="flex gap-2 items-center bg-gray-50 border border-gray-200 rounded-xl p-2 focus-within:border-agri-400 focus-within:ring-1 focus-within:ring-agri-400 transition-all"
          >
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ... (Type here)"
              className="flex-1 bg-transparent border-none focus:outline-none px-3 py-2 text-gray-800 placeholder-gray-400"
            />
            <button
              type="submit"
              disabled={loading || !input.trim()}
              className="bg-agri-600 hover:bg-agri-700 text-white p-3 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
            >
              <Send className="w-5 h-5" />
            </button>
          </form>
          <div className="text-center mt-2">
            <span className="text-[10px] text-gray-400 uppercase tracking-widest font-semibold">Text input only</span>
          </div>
        </div>
      </div>
    </div>
  );
}
