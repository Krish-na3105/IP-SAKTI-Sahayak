import './globals.css'; import Nav from '../components/Nav';
export const metadata={title:'IP-SAKTI Sahayak',description:'AI-Powered Ayurvedic IP & Compliance Navigator'};
export default function Layout({children}:{children:React.ReactNode}){return <div className="shell"><Nav/>{children}<footer className="footer"><div className="container">IP-SAKTI Sahayak • AI-assisted informational guidance • Not legal or regulatory advice.</div></footer></div>}
