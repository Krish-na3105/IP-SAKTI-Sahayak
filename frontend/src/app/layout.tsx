import './globals.css';
import Nav from '../components/Nav';

export const metadata = {
  title: 'IP-SAKTI Sahayak',
  description: 'AI-Powered Ayurvedic IP & Compliance Navigator'
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Nav />
        {children}
      </body>
    </html>
  );
}
