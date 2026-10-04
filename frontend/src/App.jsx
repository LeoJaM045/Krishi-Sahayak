import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { Sprout, MessageSquare, BookOpen, BarChart3, Globe2 } from 'lucide-react';
import Chatbot from './components/Chatbot';
import CropGuide from './components/CropGuide';
import Resources from './components/Resources';
import Analytics from './components/Analytics';

function Navigation() {
  const location = useLocation();
  const isActive = (path) => location.pathname === path ? 'bg-agri-100 text-agri-700' : 'text-gray-600 hover:bg-gray-100';

  return (
    <nav className="w-64 bg-white border-r border-gray-200 h-screen hidden md:flex flex-col sticky top-0">
      <div className="p-6">
        <div className="flex items-center gap-3 text-agri-600 mb-2">
          <Sprout className="w-8 h-8" />
          <h1 className="text-xl font-bold">Krishi Sahayak</h1>
        </div>
        <p className="text-xs text-gray-500 font-medium">ਪੰਜਾਬੀ ਕਿਸਾਨਾਂ ਲਈ ਡਿਜੀਟਲ ਸਹਾਇਕ</p>
      </div>
      
      <div className="flex-1 px-4 space-y-2 mt-4">
        <Link to="/" className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${isActive('/')}`}>
          <MessageSquare className="w-5 h-5" />
          <span className="font-medium">Chatbot</span>
        </Link>
        <Link to="/crops" className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${isActive('/crops')}`}>
          <Sprout className="w-5 h-5" />
          <span className="font-medium">Crop Guide</span>
        </Link>
        <Link to="/resources" className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${isActive('/resources')}`}>
          <BookOpen className="w-5 h-5" />
          <span className="font-medium">Resources</span>
        </Link>
        <Link to="/analytics" className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-colors ${isActive('/analytics')}`}>
          <BarChart3 className="w-5 h-5" />
          <span className="font-medium">Analytics</span>
        </Link>
      </div>

      <div className="p-4 border-t border-gray-100">
        <div className="bg-agri-50 p-4 rounded-xl border border-agri-100">
          <p className="text-xs text-agri-700 leading-relaxed text-center">
            This chatbot provides general information. Always consult a local agricultural expert for pesticide dosages.
          </p>
        </div>
      </div>
    </nav>
  );
}

function MobileNav() {
  return (
    <div className="md:hidden flex items-center justify-between p-4 bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="flex items-center gap-2 text-agri-600">
        <Sprout className="w-6 h-6" />
        <h1 className="text-lg font-bold">Krishi Sahayak</h1>
      </div>
      <div className="flex gap-4">
        <Link to="/" className="text-gray-600"><MessageSquare className="w-5 h-5" /></Link>
        <Link to="/crops" className="text-gray-600"><Sprout className="w-5 h-5" /></Link>
        <Link to="/resources" className="text-gray-600"><BookOpen className="w-5 h-5" /></Link>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="flex min-h-screen bg-gray-50">
        <Navigation />
        <main className="flex-1 flex flex-col min-h-screen max-w-full overflow-hidden">
          <MobileNav />
          <div className="flex-1 overflow-auto p-4 md:p-8">
            <Routes>
              <Route path="/" element={<Chatbot />} />
              <Route path="/crops" element={<CropGuide />} />
              <Route path="/resources" element={<Resources />} />
              <Route path="/analytics" element={<Analytics />} />
            </Routes>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
