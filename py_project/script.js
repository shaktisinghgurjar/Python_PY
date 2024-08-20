document.addEventListener("DOMContentLoaded", () => {
    const dragon = document.getElementById("dragon");
    const segments = document.querySelectorAll(".segment");

    const segmentPositions = Array.from(segments).map(() => ({ x: 0, y: 0 }));
    const segmentSpacing = 50;
    const followSpeed = 0.1;

    document.addEventListener("mousemove", (e) => {
        const mouseX = e.clientX;
        const mouseY = e.clientY;

        segmentPositions[0] = { x: mouseX, y: mouseY };

        for (let i = 1; i < segmentPositions.length; i++) {
            const prevPos = segmentPositions[i - 1];
            const currPos = segmentPositions[i];

            const dx = prevPos.x - currPos.x;
            const dy = prevPos.y - currPos.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance > segmentSpacing) {
                const angle = Math.atan2(dy, dx);
                segmentPositions[i] = {
                    x: prevPos.x - Math.cos(angle) * segmentSpacing,
                    y: prevPos.y - Math.sin(angle) * segmentSpacing,
                };
            }
        }

        segments.forEach((segment, index) => {
            const pos = segmentPositions[index];
            segment.style.transform = `translate(${pos.x}px, ${pos.y}px)`;
        });
    });
});
