"use client";

import React, { useState, useEffect, useRef } from 'react';
import {
  User, Search, GraduationCap, Briefcase, Award, Clock, AlertTriangle,
  CheckCircle, Zap, MessageSquare, Send, ChevronRight, X
} from 'lucide-react';
import {
  Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer
} from 'recharts';

export default function PlacementGPT() {
  const [students, setStudents] = useState([]);
  const [companies, setCompanies] = useState({});
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [selectedCompanyKey, setSelectedCompanyKey] = useState('TCS');
  const [evaluation, setEvaluation] = useState(null);
  const [chatMessages, setChatMessages] = useState([
    { role: 'system', content: 'Welcome to PlacementGPT. Select a student and a company to see eligibility, or ask me any career guidance questions!' }
  ]);
  const [chatInput, setChatInput] = useState('');
  const [loadingEval, setLoadingEval] = useState(false);
  const [loadingChat, setLoadingChat] = useState(false);
  const messagesEndRef = useRef(null);

  // Fetch initial data
  useEffect(() => {
    fetch('http://localhost:8000/api/students')
      .then(res => res.json())
      .then(data => {
        setStudents(data);
        if (data.length > 0) setSelectedStudent(data[0]);
      });
    fetch('http://localhost:8000/api/companies')
      .then(res => res.json())
      .then(data => setCompanies(data));
  }, []);

  // Fetch evaluation when student or company changes
  useEffect(() => {
    if (selectedStudent && selectedCompanyKey) {
      setLoadingEval(true);
      fetch('http://localhost:8000/api/evaluate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ student_id: selectedStudent.id, company_key: selectedCompanyKey })
      })
        .then(res => res.json())
        .then(data => {
          setEvaluation(data);
          setLoadingEval(false);
        });
    }
  }, [selectedStudent, selectedCompanyKey]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages]);

  const handleChatSubmit = async (e) => {
    e.preventDefault();
    if (!chatInput.trim()) return;

    const userMsg = chatInput.trim();
    setChatMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setChatInput('');
    setLoadingChat(true);

    try {
      const res = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          student_id: selectedStudent?.id,
          company_key: selectedCompanyKey,
          question: userMsg
        })
      });
      const data = await res.json();
      setChatMessages(prev => [...prev, { role: 'system', content: data.response }]);
    } catch (err) {
      setChatMessages(prev => [...prev, { role: 'system', content: 'Error connecting to PlacementGPT Backend.' }]);
    } finally {
      setLoadingChat(false);
    }
  };

  if (!selectedStudent || !evaluation) return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-cyan-400"></div>
    </div>
  );

  const radarData = [
    { subject: 'CGPA', A: (selectedStudent.cgpa / 10) * 100, fullMark: 100 },
    { subject: 'Coding', A: selectedStudent.coding, fullMark: 100 },
    { subject: 'Technical', A: selectedStudent.technical, fullMark: 100 },
    { subject: 'Aptitude', A: selectedStudent.aptitude, fullMark: 100 },
    { subject: 'Comm.', A: selectedStudent.communication, fullMark: 100 },
  ];

  const badgeClass = {
    'Eligible': 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
    'Partially Eligible': 'bg-amber-500/10 text-amber-400 border-amber-500/30',
    'Not Eligible': 'bg-red-500/10 text-red-400 border-red-500/30'
  }[evaluation.eligibility] || 'bg-gray-500/10 text-gray-400 border-gray-500/30';

  return (
    <div className="min-h-screen p-4 md:p-6 lg:p-8 flex flex-col gap-6 max-w-[1600px] mx-auto">
      {/* Header */}
      <header className="flex justify-between items-center glass-panel px-6 py-4 rounded-2xl">
        <div className="flex items-center gap-3">
          <div className="bg-gradient-to-tr from-cyan-500 to-violet-500 p-2 rounded-xl">
            <GraduationCap className="text-white w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-violet-400">PlacementGPT</h1>
            <p className="text-xs text-white/50">AI Eligibility & Career Guidance Assistant</p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <select
            className="bg-black/50 border border-white/10 rounded-lg px-4 py-2 text-sm focus:outline-none focus:border-cyan-500 transition-colors"
            value={selectedStudent.id}
            onChange={(e) => setSelectedStudent(students.find(s => s.id === e.target.value))}
          >
            {students.map(s => (
              <option key={s.id} value={s.id}>{s.name} ({s.id})</option>
            ))}
          </select>
        </div>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-grow">

        {/* Left/Middle Column: Dashboard */}
        <div className="lg:col-span-2 flex flex-col gap-6">

          {/* Top Stats Row */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="glass-card p-5 rounded-2xl flex flex-col justify-center items-center relative overflow-hidden">
              <div className="text-xs text-white/60 mb-2 font-medium tracking-wide uppercase">Readiness Score</div>
              <div className="text-5xl font-bold text-white relative z-10">
                {evaluation.readiness_score}
                <span className="text-xl text-white/40">/100</span>
              </div>
              {/* Decorative glow */}
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-24 h-24 bg-cyan-500/20 blur-2xl rounded-full"></div>
            </div>

            <div className="glass-card p-5 rounded-2xl md:col-span-2">
              <div className="flex items-start gap-4">
                <div className="p-3 bg-white/5 rounded-xl border border-white/10">
                  <User className="text-cyan-400 w-8 h-8" />
                </div>
                <div>
                  <h2 className="text-2xl font-bold">{selectedStudent.name}</h2>
                  <div className="text-sm text-white/60 mt-1 flex flex-wrap gap-x-4 gap-y-1">
                    <span>Dept: {selectedStudent.dept}</span>
                    <span>CGPA: <strong className="text-white">{selectedStudent.cgpa}</strong></span>
                    <span>Backlogs: <strong className={selectedStudent.backlogs > 0 ? "text-red-400" : "text-emerald-400"}>{selectedStudent.backlogs}</strong></span>
                  </div>
                </div>
              </div>
              <div className="mt-4 grid grid-cols-4 gap-2">
                <div className="bg-black/30 p-2 rounded-lg text-center">
                  <div className="text-[10px] text-white/50 uppercase">Coding</div>
                  <div className="font-semibold text-cyan-400">{selectedStudent.coding}</div>
                </div>
                <div className="bg-black/30 p-2 rounded-lg text-center">
                  <div className="text-[10px] text-white/50 uppercase">Projects</div>
                  <div className="font-semibold text-violet-400">{selectedStudent.projects}</div>
                </div>
                <div className="bg-black/30 p-2 rounded-lg text-center">
                  <div className="text-[10px] text-white/50 uppercase">Internships</div>
                  <div className="font-semibold text-emerald-400">{selectedStudent.internships}</div>
                </div>
                <div className="bg-black/30 p-2 rounded-lg text-center">
                  <div className="text-[10px] text-white/50 uppercase">Attendance</div>
                  <div className="font-semibold text-amber-400">{selectedStudent.attendance}%</div>
                </div>
              </div>
            </div>

            <div className="glass-card p-5 rounded-2xl flex flex-col justify-center items-center">
              <ResponsiveContainer width="100%" height={120}>
                <RadarChart cx="50%" cy="50%" outerRadius="70%" data={radarData}>
                  <PolarGrid stroke="rgba(255,255,255,0.1)" />
                  <PolarAngleAxis dataKey="subject" tick={{ fill: 'rgba(255,255,255,0.5)', fontSize: 10 }} />
                  <Radar name="Student" dataKey="A" stroke="#00f0ff" fill="#00f0ff" fillOpacity={0.2} />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Company Evaluation Row */}
          <div className="glass-panel rounded-2xl overflow-hidden flex flex-col">
            <div className="bg-white/[0.02] border-b border-white/5 p-4 flex justify-between items-center">
              <h3 className="font-bold flex items-center gap-2">
                <Briefcase className="w-4 h-4 text-cyan-400" />
                Company Eligibility Check
              </h3>
              <select
                className="bg-black/50 border border-white/10 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-cyan-500 transition-colors"
                value={selectedCompanyKey}
                onChange={(e) => setSelectedCompanyKey(e.target.value)}
              >
                {Object.keys(companies).map(k => (
                  <option key={k} value={k}>{k}</option>
                ))}
              </select>
            </div>

            <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <div className="flex items-center gap-4 mb-6">
                  <div className="text-4xl">{evaluation.company.logo}</div>
                  <div>
                    <h4 className="text-xl font-bold">{evaluation.company.name}</h4>
                    <p className="text-xs text-white/50">{evaluation.company.tier} • {evaluation.company.package}</p>
                  </div>
                  <div className={`ml-auto border px-3 py-1 rounded-full text-xs font-bold ${badgeClass}`}>
                    {evaluation.eligibility.toUpperCase()}
                  </div>
                </div>

                <div className="space-y-3">
                  {evaluation.criteria.map((c, idx) => (
                    <div key={idx} className={`flex items-center justify-between p-3 rounded-lg border ${c.met ? 'bg-emerald-500/5 border-emerald-500/10' : 'bg-red-500/5 border-red-500/10'}`}>
                      <div className="flex items-center gap-2">
                        {c.met ? <CheckCircle className="w-4 h-4 text-emerald-400" /> : <X className="w-4 h-4 text-red-400" />}
                        <span className="text-sm text-white/90">{c.label}</span>
                      </div>
                      <div className="text-right">
                        <div className="text-[10px] text-white/40">Req: {c.required}</div>
                        <div className={`text-sm font-semibold ${c.met ? 'text-emerald-400' : 'text-red-400'}`}>{c.actual}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="flex flex-col gap-6">
                <div>
                  <h4 className="text-sm font-bold text-white/80 mb-3 flex items-center gap-2">
                    <Zap className="w-4 h-4 text-amber-400" /> Strengths
                  </h4>
                  <ul className="space-y-2">
                    {evaluation.strengths.slice(0, 3).map((s, i) => (
                      <li key={i} className="text-sm text-white/60 flex items-start gap-2">
                        <span className="text-emerald-400 mt-1">•</span> {s}
                      </li>
                    ))}
                  </ul>
                </div>

                <div>
                  <h4 className="text-sm font-bold text-white/80 mb-3 flex items-center gap-2">
                    <AlertTriangle className="w-4 h-4 text-red-400" /> Areas to Improve
                  </h4>
                  <ul className="space-y-2">
                    {evaluation.weaknesses.slice(0, 3).map((w, i) => (
                      <li key={i} className="text-sm text-white/60 flex items-start gap-2">
                        <span className="text-red-400 mt-1">•</span> {w}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Chatbot */}
        <div className="glass-panel rounded-2xl flex flex-col h-[800px] overflow-hidden">
          <div className="bg-gradient-to-r from-cyan-900/40 to-violet-900/40 border-b border-white/5 p-4 flex items-center gap-3">
            <div className="bg-cyan-500/20 p-2 rounded-lg">
              <MessageSquare className="w-5 h-5 text-cyan-400" />
            </div>
            <div>
              <h3 className="font-bold text-white">PlacementGPT Agent</h3>
              <p className="text-[10px] text-cyan-400/80">Llama 3.2 1B Instruct Simulation</p>
            </div>
          </div>

          <div className="flex-grow p-4 overflow-y-auto flex flex-col gap-4 relative custom-scrollbar">
            {chatMessages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${msg.role === 'user'
                    ? 'bg-gradient-to-r from-cyan-500 to-violet-500 text-white rounded-tr-none'
                    : 'glass-card border-white/10 text-white/90 rounded-tl-none whitespace-pre-wrap'
                  }`}>
                  {msg.content}
                </div>
              </div>
            ))}
            {loadingChat && (
              <div className="flex justify-start">
                <div className="glass-card rounded-2xl rounded-tl-none px-4 py-3 border-white/10 flex items-center gap-2">
                  <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce delay-75"></div>
                  <div className="w-2 h-2 bg-cyan-400 rounded-full animate-bounce delay-150"></div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="p-4 bg-white/[0.02] border-t border-white/5">
            <form onSubmit={handleChatSubmit} className="relative">
              <input
                type="text"
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                placeholder={`Ask about ${selectedStudent.name}'s readiness...`}
                className="w-full bg-black/40 border border-white/10 rounded-xl pl-4 pr-12 py-3 text-sm focus:outline-none focus:border-cyan-500 transition-all text-white placeholder-white/30"
              />
              <button
                type="submit"
                disabled={loadingChat || !chatInput.trim()}
                className="absolute right-2 top-1/2 -translate-y-1/2 p-2 bg-cyan-500/20 text-cyan-400 hover:bg-cyan-500/40 hover:text-white rounded-lg transition-colors disabled:opacity-50"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
          </div>
        </div>

      </div>
    </div>
  );
}
