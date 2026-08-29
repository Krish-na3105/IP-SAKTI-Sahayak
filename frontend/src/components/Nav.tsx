'use client';

import Link from 'next/link';

export default function Nav() {
  return (
    <>
      {/* <div className="demoBar">
        DEMO DATA • SIH 2026 V1 PROTOTYPE • SYNTHETIC PATENT/TK RECORDS
      </div> */}

      <nav className="nav">
        <Link className="brand" href="/">
          <img src="/logo.png" alt="logo" className="logo" />
          <span>IP-SAKTI Sahayak</span>
        </Link>

        <div className="navlinks">
          <Link href="/assessment">Product Assessment</Link>
          <Link href="/patents">Patent Search</Link>
          <Link href="/cost">Cost Estimator</Link>
          <Link href="/knowledge">Knowledge Base</Link>
          <Link href="/ask">Ask AI</Link>

          <Link className="btn primary" href="/assessment">
            Start Assessment
          </Link>
        </div>

        <span className="badge">🇮🇳 India</span>
      </nav>
    </>
  );
}