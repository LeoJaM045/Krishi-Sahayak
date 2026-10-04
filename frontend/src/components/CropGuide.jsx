import React, { useState, useEffect } from 'react';
import { Loader2, Search, Thermometer, Droplets, ShieldAlert, Sprout } from 'lucide-react';
import { api } from '../utils/api';

const CropCard = ({ name, data, onClick }) => (
  <div 
    onClick={() => onClick(name, data)}
    className="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-md hover:border-agri-200 cursor-pointer transition-all hover:-translate-y-1 group"
  >
    <div className="flex justify-between items-start mb-4">
      <div>
        <h3 className="text-2xl font-bold text-gray-800">{data.name_punjabi}</h3>
        <p className="text-gray-500 font-medium">{data.name_english}</p>
      </div>
      <div className="w-12 h-12 rounded-full bg-agri-50 flex items-center justify-center text-agri-600 group-hover:bg-agri-100 transition-colors">
        <Sprout className="w-6 h-6" />
      </div>
    </div>
    
    <div className="space-y-2 mt-4 text-sm text-gray-600">
      <div className="flex items-center gap-2">
        <Thermometer className="w-4 h-4 text-agri-500" />
        <span className="truncate">{data.sowing_period.split('(')[0]}</span>
      </div>
      <div className="flex items-center gap-2">
        <Droplets className="w-4 h-4 text-blue-500" />
        <span className="truncate">{data.irrigation.split('(')[0]}</span>
      </div>
    </div>
  </div>
);

const CropDetail = ({ name, data, onBack }) => (
  <div className="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden animate-in slide-in-from-right-4 duration-300">
    <div className="bg-agri-50/50 p-6 border-b border-agri-100 flex items-center justify-between">
      <div>
        <button onClick={onBack} className="text-agri-600 hover:text-agri-800 font-medium text-sm mb-2 flex items-center gap-1">
          ← Back to Guide
        </button>
        <h2 className="text-3xl font-bold text-gray-800">{data.name_punjabi} <span className="text-xl text-gray-500 font-normal ml-2">({data.name_english})</span></h2>
      </div>
      <Sprout className="w-12 h-12 text-agri-300 opacity-50" />
    </div>
    
    <div className="p-6 grid md:grid-cols-2 gap-8">
      <div className="space-y-6">
        <div>
          <h4 className="flex items-center gap-2 font-bold text-gray-800 mb-2 border-b pb-2"><Thermometer className="w-5 h-5 text-agri-500"/> ਬਿਜਾਈ ਅਤੇ ਵਾਢੀ (Season)</h4>
          <p className="text-gray-700 text-sm leading-relaxed"><span className="font-semibold text-gray-900">Sowing:</span> {data.sowing_period}</p>
          <p className="text-gray-700 text-sm leading-relaxed mt-1"><span className="font-semibold text-gray-900">Harvesting:</span> {data.harvesting_period}</p>
        </div>
        <div>
          <h4 className="flex items-center gap-2 font-bold text-gray-800 mb-2 border-b pb-2"><Droplets className="w-5 h-5 text-blue-500"/> ਸਿੰਚਾਈ ਅਤੇ ਮਿੱਟੀ (Soil & Water)</h4>
          <p className="text-gray-700 text-sm leading-relaxed"><span className="font-semibold text-gray-900">Soil:</span> {data.soil_requirements}</p>
          <p className="text-gray-700 text-sm leading-relaxed mt-1"><span className="font-semibold text-gray-900">Irrigation:</span> {data.irrigation}</p>
        </div>
      </div>
      <div className="space-y-6">
        <div>
          <h4 className="flex items-center gap-2 font-bold text-gray-800 mb-2 border-b pb-2"><Sprout className="w-5 h-5 text-green-600"/> ਖਾਦ (Fertilizer)</h4>
          <p className="text-gray-700 text-sm leading-relaxed">{data.fertilizer}</p>
        </div>
        <div>
          <h4 className="flex items-center gap-2 font-bold text-gray-800 mb-2 border-b pb-2"><ShieldAlert className="w-5 h-5 text-red-500"/> ਬਿਮਾਰੀਆਂ ਅਤੇ ਕੀੜੇ (Pests & Diseases)</h4>
          <p className="text-gray-700 text-sm leading-relaxed"><span className="font-semibold text-gray-900">Pests:</span> {data.common_pests.join(", ")}</p>
          <p className="text-gray-700 text-sm leading-relaxed mt-1"><span className="font-semibold text-gray-900">Diseases:</span> {data.common_diseases.join(", ")}</p>
          <p className="text-gray-700 text-sm leading-relaxed mt-2 p-3 bg-red-50 text-red-800 rounded-lg border border-red-100">{data.basic_prevention}</p>
        </div>
      </div>
    </div>
  </div>
);

export default function CropGuide() {
  const [crops, setCrops] = useState({});
  const [loading, setLoading] = useState(true);
  const [selectedCrop, setSelectedCrop] = useState(null);
  const [search, setSearch] = useState('');

  useEffect(() => {
    api.getCrops()
      .then(res => setCrops(res.crops || {}))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <div className="flex h-full items-center justify-center"><Loader2 className="w-8 h-8 animate-spin text-agri-500" /></div>;
  }

  if (selectedCrop) {
    return <CropDetail name={selectedCrop.name} data={selectedCrop.data} onBack={() => setSelectedCrop(null)} />;
  }

  const filteredCrops = Object.entries(crops).filter(([name, data]) => 
    name.includes(search) || data.name_english.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="max-w-6xl mx-auto pb-10">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <div>
          <h2 className="text-3xl font-bold text-gray-800">Crop Guide</h2>
          <p className="text-gray-500">Detailed information about major crops in Punjab</p>
        </div>
        <div className="relative w-full md:w-72">
          <Search className="w-5 h-5 absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
          <input 
            type="text" 
            placeholder="Search crops..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full bg-white border border-gray-200 pl-10 pr-4 py-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-agri-400 transition-all shadow-sm"
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredCrops.map(([name, data]) => (
          <CropCard key={name} name={name} data={data} onClick={(n, d) => setSelectedCrop({name: n, data: d})} />
        ))}
      </div>
      
      {filteredCrops.length === 0 && (
        <div className="text-center py-20 text-gray-500 bg-white rounded-2xl border border-gray-100 border-dashed">
          No crops found matching "{search}"
        </div>
      )}
    </div>
  );
}
