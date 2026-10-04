import React from 'react';
import { BookOpen, Droplets, MapPin, PhoneCall, ShieldCheck, Sun } from 'lucide-react';

export default function Resources() {
  const links = [
    { title: "Punjab Agricultural University (PAU)", url: "https://www.pau.edu/", icon: <BookOpen className="w-6 h-6" /> },
    { title: "Kisan Call Center", url: "#", desc: "Toll Free: 1800-180-1551", icon: <PhoneCall className="w-6 h-6" /> },
    { title: "Department of Agriculture, Punjab", url: "http://agripb.gov.in/", icon: <MapPin className="w-6 h-6" /> },
    { title: "PM Fasal Bima Yojana", url: "https://pmfby.gov.in/", icon: <ShieldCheck className="w-6 h-6" /> },
    { title: "Soil Health Card Scheme", url: "https://soilhealth.dac.gov.in/", icon: <Droplets className="w-6 h-6" /> },
    { title: "Mausam (IMD)", url: "https://mausam.imd.gov.in/", icon: <Sun className="w-6 h-6" /> },
  ];

  return (
    <div className="max-w-4xl mx-auto">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-gray-800">Farming Resources</h2>
        <p className="text-gray-500 mt-1">Important links and contacts for farmers in Punjab</p>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        {links.map((link, i) => (
          <a 
            key={i} 
            href={link.url} 
            target="_blank" 
            rel="noopener noreferrer"
            className="flex items-center gap-4 bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md hover:border-agri-300 transition-all group"
          >
            <div className="w-14 h-14 bg-agri-50 rounded-xl flex items-center justify-center text-agri-600 group-hover:bg-agri-600 group-hover:text-white transition-colors">
              {link.icon}
            </div>
            <div>
              <h3 className="font-bold text-gray-800 group-hover:text-agri-700 transition-colors">{link.title}</h3>
              {link.desc && <p className="text-sm text-gray-500 font-medium">{link.desc}</p>}
            </div>
          </a>
        ))}
      </div>

      <div className="mt-10 bg-blue-50 p-6 rounded-2xl border border-blue-100 flex gap-4">
        <div className="text-blue-500 mt-1"><ShieldCheck className="w-8 h-8"/></div>
        <div>
          <h3 className="font-bold text-blue-900 text-lg">Disclaimer / ਚਿਤਾਵਨੀ</h3>
          <p className="text-blue-800 text-sm mt-2 leading-relaxed">
            ਇਹ ਐਪਲੀਕੇਸ਼ਨ ਸਿਰਫ ਆਮ ਜਾਣਕਾਰੀ ਲਈ ਹੈ। ਖਾਦਾਂ ਅਤੇ ਕੀਟਨਾਸ਼ਕਾਂ ਦੀ ਸਹੀ ਮਾਤਰਾ ਲਈ ਹਮੇਸ਼ਾ PAU ਮਾਹਿਰਾਂ, KVK ਜਾਂ ਖੇਤੀਬਾੜੀ ਅਧਿਕਾਰੀ ਦੀ ਸਲਾਹ ਲਓ। (This application is for general information only. Always consult PAU experts, KVK, or agriculture officers for exact fertilizer and pesticide doses.)
          </p>
        </div>
      </div>
    </div>
  );
}
