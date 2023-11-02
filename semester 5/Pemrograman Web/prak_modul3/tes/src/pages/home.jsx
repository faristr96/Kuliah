import "bootstrap/dist/css/bootstrap.min.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import HeroHome from "../components/Home";

const Home = () => {
  return (
    <>
      <Navbar />
      <HeroHome />
      {/* <main className="my-5 py-5">
        <h1>Home Page</h1>
      </main> */}
      <Footer />
    </>
  );
};

export default Home;